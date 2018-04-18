class CreateGames < ActiveRecord::Migration[5.1]
  def change
    create_table :games do |t|
      t.string :name
      t.text :thumbnail
      t.text :url

      t.timestamps
    end
  end
end
