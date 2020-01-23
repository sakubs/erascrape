"""
This is a module for making a little SQLite DB based on the era information 
so that I don't need to keep pinging the poor website, and also for more 
useful lookups and integration into other projects.

It's totally optional to use this module, I am including it in case 
somebody else decides to use this library and finds it useful.
"""
import sqlite3

ERASCRAPE_DB = 'resources/erascrapedb.db3'

def create_connection(dbpath):
    conn = None
    try:
        conn = sqlite3.connect(dbpath)
        return conn
    except sqlite3.Error as e:
        print(e)

def create_table(conn):
    sql = """CREATE TABLE japanese_eras (
        name text NOT NULL, 
        start_date text NOT NULL, 
        end_date text, 
        id integer PRIMARY_KEY)"""
    
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_era(conn, record):
    cur = conn.cursor()
    sql = "INSERT OR IGNORE INTO japanese_eras VALUES ({seq})".format(seq=','.join(['?']*len(record)))
    cur.execute(sql, record)
    return cur.lastrowid

def find_era_by_date(conn, querydate):
    cur = conn.cursor()

    sql = "SELECT * WHERE "
    return cur.fetchall()