import csv, sqlite3

# Create the database
connection = sqlite3.connect('hosts.sqlite')
cursor = connection.cursor()

# Create the table
cursor.execute('DROP TABLE IF EXISTS Hosts')
cursor.execute('CREATE TABLE Hosts ( Hostname text, Location text, Something text) ')

connection.commit()

# Load the CSV file into CSV reader
csvfile = open('hosts.csv', 'rb')
creader = csv.reader(csvfile, delimiter=',', quotechar='|')

# Iterate through the CSV reader, inserting values into the database
for t in creader:
	cursor.execute('INSERT INTO Hosts VALUES (?,?,?)', t )

# Close the csv file, commit changes, and close the connection
csvfile.close()
connection.commit()
connection.close()
