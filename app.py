from flask import Flask, render_template, request, abort, make_response
from flaskext.mysql import MySQL
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_pyfile('config.ini')
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def index():
    return '<html>I am Erogamescape Recommender System</html>'

@app.route('/recommendation/personalized/<user_id>')
def recommendation_personalized(user_id):
    cursor = mysql.connect().cursor()
    cursor.execute('''
    select game_id from recommendation_personalized where user_id = "{0}" limit 5
    '''.format(user_id))
    game_ids =  [game_id for game_id, in cursor.fetchall()] # tuple なので gameid, とする
    if len(game_ids) == 0:
        rendered = render_template('recommendation_personalized_none.html')
    else:
        game_htmls = [requests.get('{0}{1}'.format(app.config['GAME_URL'], game_id)).content.decode('utf-8')
                      for game_id in game_ids]
        game_images = [BeautifulSoup(game_html, 'lxml').select('#main_image > a > img')[0]['src']
                       for game_html in game_htmls]
        game_titles = [BeautifulSoup(game_html, 'lxml').select('#soft-title > span')[0].text
                       for game_html in game_htmls]
        games = [
            {'id': id, 'image': image, 'title': title}
            for id, image, title in zip(game_ids, game_images, game_titles)
        ]
        rendered = render_template('recommendation_personalized.html',
                                   games=games, game_url=app.config['GAME_URL'] )
    response = make_response(rendered)
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

@app.route('/admin/recommendation/personalized', methods=['POST'])
def admin_recommendation_personalized():
    if request.form['passwd'] != app.config['ADMIN_PASSWD']:
        abort(404)
    user_id, game_id, prediction = request.form['user_id'], request.form['game_id'], request.form['prediction']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''
    delete from recommendation_personalized where user_id = "{0}" and game_id = {1}
    '''.format(user_id, game_id))
    cursor.execute('''
    insert into recommendation_personalized values("{0}", {1}, {2})
    '''.format(user_id, game_id, prediction))
    conn.commit()
    return 'accepted'

if __name__ == '__main__':
    app.run()
