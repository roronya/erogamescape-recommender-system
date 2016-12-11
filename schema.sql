drop table recommendation_personalized;

create table recommendation_personalized(
  user_id varchar(1024),
  game_id integer,
  prediction integer
);

alter table recommendation_personalized add index index_name(user_id);