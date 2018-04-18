FROM ruby:2.5

WORKDIR /app

RUN apt-get update && \
    apt-get install -y mysql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo 'gem: --no-document' >> ~/.gemrc && \
    bundle config --global jobs 4

RUN gem install bundler

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

EXPOSE 3000

CMD ["bin/rails", "s", "-b", "0.0.0.0"]
