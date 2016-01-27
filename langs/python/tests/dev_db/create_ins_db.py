import sqlite3,csv

conn = sqlite3.connect('hosts.sqlite')
cur = conn.cursor()

#cur.execute('''DROP TABLE IF EXISTS Hosts''') 

cur.execute('''
CREATE TABLE IF NOT EXISTS Hosts (Hostname TEXT UNIQUE, Location INTEGER UNIQUE, Position TEXT)''')

f_host = 'hosts.csv'
f_tloc = 'location.csv'

with open(f_host, 'rb') as hfile, open(f_tloc, 'rb') as tfile:

    hreader = csv.reader(hfile)
    treader = csv.reader(tfile)

    for line_x in hreader:
        (hostname,location,something) = line_x[0], line_x[1], line_x[2]
    
        cur.execute('''REPLACE INTO Hosts (Hostname, Location) 
            VALUES ( ?, ? )''', ( hostname, location ) )
    
    for line_y in treader:
        (location_fk,random,data) = line_y[0], line_y[1], line_y[2]

        cur.execute("UPDATE Hosts SET POSITION=? WHERE Location=?",\
        (data,location_fk))

conn.commit()
cur.close()

