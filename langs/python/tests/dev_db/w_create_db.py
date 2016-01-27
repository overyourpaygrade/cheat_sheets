import sqlite3

conn = sqlite3.connect('hosts.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Hosts''') 

cur.execute('''
CREATE TABLE Hosts (Hostname TEXT, Location INTEGER, Position TEXT)''')

f_host = open('hosts.csv')
f_tloc = open('location.csv')


for line in f_host:
#  if not line.startswith('From: ') : continue
  lp = line.split(',')
  (hostname,location,something) = lp[0], lp[1], lp[2]


  for line_y in f_tloc:
    lps = line_y.split(',')
    if location == lps[0]:
      print hostname,lps[0],lps[2].rstrip()
      cur.execute('''INSERT INTO Hosts (Hostname, Location, Position) 
        VALUES ( ?, ?, ? )''', (  hostname,lps[0],lps[2].rstrip() ) )
      break

conn.commit()
cur.close()

#  cur.execute('SELECT count FROM Hosts WHERE email = ? ', (email, ))
#  try:
#    count = cur.fetchone()[0]
#    cur.execute('UPDATE Hosts SET count=count+1 WHERE email = ?', (email, ))
#  except:
#    cur.execute('''INSERT INTO Hosts (email, count)
#      VALUES ( ?, 1 )''', ( email, ) )
#  conn.commit() #Write to disk
#    
## https://www.sqlite.org/lang_select.html
#sqlstr = 'SELECT email, count FROM Hosts ORDER BY count DESC LIMIT 10'
#
#for row in cur.execute(sqlstr):
#  print str(row[0]), row[1]
  
