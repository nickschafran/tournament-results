/*
tournament.sql 
creates database and establishes schema for Swiss-sytem tournament
*/

-- drop previously created tournament database
drop database tournament;

-- create and connect to tournament database 
create database tournament;
\c tournament;

-- create players table
create table players (
    id serial primary key, 
    name text
);

-- create matches table
create table matches (
    id serial primary key, 
    winner serial references players(id),
    loser serial references players(id)
);

 -- # of matches each player has played
create view plays as
    select players.id as id, count(matches.id) as played_games 
    from players
    left join matches
    on players.id = matches.winner or players.id = matches.loser
    group by players.id
    order by played_games desc; 

-- # of matches each player has won
create view wins as
    select players.id as id, count(matches.winner) as won_games
    from players
    left join matches
    on players.id = matches.winner
    group by players.id
    order by won_games desc; 

-- view of player standings
create view standings as
    select players.id as id, players.name as name, won_games as wins, 
    played_games as matches 
    from players 
    left join wins on players.id = wins.id 
    left join plays on players.id = plays.id
    order by wins desc;
    