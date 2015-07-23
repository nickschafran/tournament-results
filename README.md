#Tournament Results
This repository contains a PostgreSQL database schema and python module utilizing Psycopg to serve an application for a [Swiss-style tournament](http://www.wizards.com/dci/downloads/swiss_pairings.pdf). It is a submission for Project 2 in [Udacity’s Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

##Instructions:
You will need to have installed [PostgreSQL](http://www.postgresql.org/) to utilize the application. Once installed, you can use the terminal command `psql -f tournament.sql` from the directory in which you have downloaded the files to build the application’s database. Having now set up the database, you can use the commands contained in the tournament.py module to manipulate the database in your tournament.

##Files Needed to Run:
* tournament.sql
* tournament.py

##References:
* Psycopg module usage tips taken from [Psycopg 2.6.1 documentation](http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries)

* Odd and even list sampling on swissPairings():
  * Python documentation on [Extended Slices]https://docs.python.org/2.3/whatsnew/section-slices.html
  * http://stackoverflow.com/a/11702449
  * http://stackoverflow.com/a/756602

* Zip function on swissPairings():
  * Python Documentation on [Zip](https://docs.python.org/2/library/functions.html#zip)
  * http://stackoverflow.com/a/24844077
