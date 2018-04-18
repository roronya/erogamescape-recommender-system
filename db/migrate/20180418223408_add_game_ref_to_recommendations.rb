class AddGameRefToRecommendations < ActiveRecord::Migration[5.1]
  def change
    add_reference :recommendations, :game, foreign_key: true
  end
end
