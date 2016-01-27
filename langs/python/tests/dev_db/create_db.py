import sqlite3

conn = sqlite3.connect('hosts.sqlite')
cur = conn.cursor()

#cur.execute('''
#DROP TABLE IF EXISTS Hosts''') 

cur.execute('''
CREATE TABLE IF NOT EXISTS Hosts (Hostname TEXT, Location INTEGER PRIMARY KEY, Position TEXT)''')

f_host = open('hosts.csv')
f_tloc = open('location.csv')

for line in f_host:
    lp = line.split(',')
    (hostname,location,something) = lp[0], lp[1], lp[2]

    for line_y in f_tloc:
      lps = line_y.split(',')
      if location == lps[0]:
        print hostname,lps[0],lps[2].rstrip()
        cur.execute('''REPLACE INTO Hosts (Hostname, Location, Position) 
            VALUES ( ?, ?, ? )''', (  hostname,lps[0],lps[2].rstrip() ) )
        break

conn.commit()
cur.close()

