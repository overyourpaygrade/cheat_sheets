#!/usr/bin/python
import sqlite3,csv,sys

try:
    conn = sqlite3.connect('hosts.sqlite')
    cur = conn.cursor()
except:
    print "Failed to connect to the database"
    sys.exit(1)

# Start Fresh
cur.execute('DROP TABLE IF EXISTS Hosts') 
cur.execute('DROP TABLE IF EXISTS Locations') 

# Create Hosts table
cur.execute('''
CREATE TABLE IF NOT EXISTS Hosts (Location INTEGER PRIMARY KEY, Hostname TEXT,
Position TEXT)''')

# Create Location table
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (Location_fk INTEGER, Random TEXT,
Data TEXT)''')

# Files to be used
f_host = 'hosts.csv'
f_tloc = 'location.csv'

with open(f_host, 'rb') as hfile, open(f_tloc, 'rb') as tfile:

    hreader = csv.reader(hfile)
    treader = csv.reader(tfile)

    for line_x in hreader:
        (hostname,location,something) = line_x[0], line_x[1], line_x[2]

        cur.execute('''REPLACE INTO Hosts (Location, Hostname, Position) 
            VALUES ( ?, ?, ? )''', ( location, hostname, something ) )

    hfile.close()

    for line_y in treader:
        (location_fk,random,data) = line_y[0], line_y[1], line_y[2]

        cur.execute('''REPLACE INTO Locations (Location_fk, Random, Data) 
            VALUES ( ?, ?, ? )''', ( location_fk, random, data ) )

    tfile.close()
            
conn.commit()
cur.close()

