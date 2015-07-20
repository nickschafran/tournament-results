#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
# Author: Nicholas Schafran, July 2015


import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cur = db.cursor()
        return db, cur
    except:
        print("Error connecting to the database")

def deleteMatches():
    """Remove all the match records from the database."""
    # Connect to database, open a cursor
    db, cur = connect()
    query = "TRUNCATE matches CASCADE;"
    # Execute query from tournament.sql
    cur.execute(query)
    # Commit changes to database
    db.commit()
    # Close cursor and connection
    cur.close()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cur = connect()
    query = "TRUNCATE players CASCADE;"
    cur.execute(query)
    db.commit()
    cur.close()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cur = connect()
    query = "SELECT count(*) AS num FROM players;"
    cur.execute(query)
    return cur.fetchone()[0]
    cur.close()
    db.close()


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    db, cur = connect()
    query = "INSERT INTO players (name) VALUES (%s)"
    param = (name,)
    cur.execute(query, param)
    db.commit()
    cur.close()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cur = connect()
    query = "SELECT * FROM standings;"
    cur.execute(query)
    return cur.fetchall()
    cur.close()
    db.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cur = connect()
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s)"
    param = (winner, loser)
    cur.execute(query, param)
    db.commit()
    cur.close()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # store results of playerStandings() in a variable
    standings = playerStandings()
    # zip together lists of even & odd players extracted from playerStandings()
    zipped = zip(standings[::2], standings[1::2])
    # create list of only ids and names from zipped, pair each up in one tuple
    pairings = [(even[0], even[1], odd[0], odd[1])
                for even, odd in list(zipped)]
    return pairings
