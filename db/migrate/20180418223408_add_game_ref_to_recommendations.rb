class AddGameRefToRecommendations < ActiveRecord::Migration[5.1]
  def change
    add_reference :recommendations, :game, foreign_key: true
    add_reference :recommendations, :recommendation, foreign_key: { to_table: :games }
  end
end
