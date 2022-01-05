import sqlite3
from scraper import Organization


## Query to Organizations
con = sqlite3.connect('crunchbase.db')
cur = con.cursor()
cur.execute("SELECT * from ORGANIZATIONS")
rows = cur.fetchall()

for row in rows:
    print(row)
