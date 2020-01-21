import sqlite3

ERASCRAPE_DB = 'resources/erascrapedb.db3'

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(ERASCRAPE_DB)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    sql = """CREATE TABLE japanese_eras (
        id integer PRIMARY_KEY, 
        name text NOT NULL, 
        start_date text NOT NULL, 
        end_date text)"""
    
    try:
        c = conn.cursor()
        c.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_era(conn, record):
    cur = conn.cursor()
    sql = "INSERT OR IGNORE INTO japanese_eras VALUES ({seq})".format(seq=','.join(['?']*len(record)))
    cur.execute(sql, record)

    return cur.fetchall()