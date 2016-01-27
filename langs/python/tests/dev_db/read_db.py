import sqlite3

# Create a connection
con = sqlite3.connect('hosts.sqlite')
cur = con.cursor()

for row in cur.execute('SELECT * FROM Hosts;'):
	print(row)

con.close()
