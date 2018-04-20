Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/games', to: 'game#index'
  get '/games/:id', to: 'game#show'
  get '/recommendations', to: 'recommendation#index'
  get '/recommendations/:id', to: 'recommendation#show'
end