#!/usr/bin/python
import sqlite3, sys, argparse, csv
import logging

def main():

    # Create a connection
    try:
        con = sqlite3.connect('hosts.sqlite')
        cur = con.cursor()
    except:
        print "Could not establish a connection with the DB"
        sys.exit(1)

    # Get arguments
    parser = argparse.ArgumentParser(description='hey')
    parser.add_argument('-o', dest='opts', help='option')
    parser.add_argument('-q', dest='query', help='query')
    parser.add_argument('-l', dest='debug', help='debug')
    args = parser.parse_args()
    
    # At least one argument check
    if not args.opts:
        print "Enter an option (all, host _hostname_, join)"
        sys.exit(1)

    # Set logging parameters
    if args.debug:

        LEVELS = { 'debug': logging.DEBUG,
                   'info' : logging.INFO
                 }
        level = LEVELS.get(args.debug.lower(), logging.NOTSET)
        logging.basicConfig(level=level)
        logger = logging.getLogger(__name__)
    
    # Dump all in selected table
    if args.opts == "all" and args.query:
        logging.debug("Option: {} -- Query: {}".format(args.opts,args.query))
        for row in cur.execute('SELECT * FROM {}'.format(args.query)):
            print(row)

    # Select host from Hosts table
    elif args.opts == "host" and args.query:
        logging.debug("Option: {} -- Query: {}".format(args.opts,args.query))
        for row in cur.execute('SELECT * FROM Hosts WHERE Hostname="{}"'.format(args.query)):
    	    print(row)

    # Join tables on key and print
    elif args.opts == "join":
        for row in cur.execute('SELECT Location, Hostname, Position, Data FROM Hosts \
            INNER JOIN Locations ON Hosts.Location = Locations.Location_fk'):
    	    print(row)

    # Join tables on key and write out to a file
    elif args.opts == "writer":
        data = cur.execute('SELECT Location, Hostname, Position, Data FROM Hosts \
            INNER JOIN Locations ON Hosts.Location = Locations.Location_fk')
        logging.debug("Data: {}".format(data))

        with open('output.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['Location', 'Hostname', 'Position', 'Data'])

            for row in data:
                writer.writerow(row)

    else:
        print "dunno"
    
    con.close()

if __name__ == '__main__':
    main()
