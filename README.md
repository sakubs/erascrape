# erascrape
A little web scraper to get the start and end dates for Japanese eras.

A simple way to get a list of up to date information on Japanese era names, 
start dates, and end dates to use in Python programs.

Just scrapes houshinji.org for the era name, start date, and end date. It 
cleans up the whitespace and returns the information as a list. What you 
choose to do with it after that is up to you.

There are database helper scripts for SQLite if you so choose to go that route.

This library is meant to be simple and have one purpose, get the names, start 
and end dates for Japanese eras from a complete and accurate source in order 
to help with developing larger projects that require this functionality.

# Installation

Using pip or pipenv:

pipenv install git+https://github.com/sakubs/erascrape#egg=erascrape

or

pip install git+https://github.com/sakubs/erascrape#egg=erascrape

# Usage

Import the library in your module:

import erascrape

or 

from erascrape import scrape

or if you want to use an sqlite db to store the data:

from erascrape import scrape, dbhandler

# Contributing
If you want to help me out with documentation, or bug fixing, or 
maintenance I would be happy to accept as long as it's within the 
scope of the simple function and purpose of this library.   