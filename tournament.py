#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
# Nicholas Schafran
#
# July 2015


import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    # Connect to database
    conn = connect()
    # Opens a cursor
    cur = conn.cursor()
    query = "delete from matches;"
    # Execute query from tournament.sql
    cur.execute(query)
    # Commit changes to database
    conn.commit()
    # Close cursor and connection
    cur.close()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cur = conn.cursor()
    query = "delete from players;"
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cur = conn.cursor()
    query = "select count (*) as num from players;"
    cur.execute(query)
    return cur.fetchone()[0]
    cur.close()
    conn.close()


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cur = conn.cursor()
    query = "insert into players (name) values (%s)"
    param = (name,)
    cur.execute(query, param)
    conn.commit()
    cur.close()
    conn.close()


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
    conn = connect()
    cur = conn.cursor()
    query = "select * from standings;"
    cur.execute(query)
    return cur.fetchall()
    cur.close()
    conn.close()


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cur = conn.cursor()
    query = "insert into matches (winner, loser) values (%s, %s)"
    param = (winner, loser)
    cur.execute(query, param)
    conn.commit()
    conn.close()


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
