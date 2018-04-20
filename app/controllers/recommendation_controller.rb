class RecommendationController < ApplicationController
  def index
    @recommendations = Recommendation.all
    render json: @recommendations
  end

  def show
    @recommendations = Recommendation.find_by(game_id=params[:game_id])
    render json: @recommendatipons
  end
end
