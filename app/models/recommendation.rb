class Recommendation < ApplicationRecord
  has_many :recommendation, class_name: 'Game', foreign_key: :game_id
end
