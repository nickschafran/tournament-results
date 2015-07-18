/*

tournament.sql -- creates db & establishes schema for Swiss-sytem tournament

Author: Nicholas Schafran, July 2015

*/

-- drop previously created tournament database
DROP DATABASE tournament;

-- create and connect to tournament database
CREATE DATABASE tournament;
\c tournament;

-- create players table
CREATE TABLE players (
    id serial PRIMARY KEY,
    name text
);

-- create matches table
CREATE TABLE matches (
    id serial PRIMARY KEY,
    winner serial REFERENCES players(id),
    loser serial REFERENCES players(id)
);

 -- # of matches each player has played
CREATE VIEW plays AS
    SELECT players.id AS id, count(matches.id) AS played_games
    FROM players
    LEFT JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
    GROUP BY players.id
    ORDER BY played_games DESC;

-- # of matches each player has won
CREATE VIEW wins AS
    SELECT players.id AS id, count(matches.winner) AS won_games
    FROM players
    LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id
    ORDER BY won_games DESC;

-- view of player standings
CREATE VIEW standings AS
    SELECT players.id AS id, players.name AS name, won_games AS wins,
    played_games AS matches
    FROM players
    LEFT JOIN wins ON players.id = wins.id
    LEFT JOIN plays ON players.id = plays.id
    ORDER BY wins DESC;
    