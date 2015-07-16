#Tournament Results
This repository contains a PostgreSQL database schema and python module utilizing Psycopg to serve an application for a [Swiss-style tournament](http://www.wizards.com/dci/downloads/swiss_pairings.pdf). It is a submission for Project 2 in [Udacity’s Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

##Instructions:
To utilize the application, you will need to install [PostgreSQL](http://www.postgresql.org/). Once installed, you can use the commands psql and \i tournament.sql from the directory in which you have downloaded the files to build the application’s database. Having now set up the database, you can use the commands contained in the python module to manipulate the database in your tournament.

##Files Contained:
* tournament.sql
* tournament.py

##Citations:
* Psycopg module usage tips taken from [Psycopg 2.6.1 documentation](http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries)

* tournament.sql schema took inspiration from [SQL: Using Views to Make Complex Queries Manageable](https://plus.google.com/u/0/events/cs0lddl0stv1mjk4a5kruslmsmg)

* Odd and even list sampling on swissPairings():
  * http://stackoverflow.com/a/11702449
  * http://stackoverflow.com/a/756602
  * https://docs.python.org/2.3/whatsnew/section-slices.html

* Zip function on swissPairings():
  * Used suggestion from [Tournament Results: Getting Started](https://docs.google.com/a/knowlabs.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true)
  * Python Documentation on [Zip](https://docs.python.org/2/library/functions.html#zip)
  * http://stackoverflow.com/a/24844077

