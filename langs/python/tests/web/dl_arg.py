#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TO ADD:
# url parser based on series? dictionary based downloader
# progress bar?
# Handle bad link

import urllib2
import requests
import argparse
import logging
from bs4 import BeautifulSoup

def soupify(url):
    logging.debug("Soupify: {}".format(url))

    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")
    except:
        print "Error loading webpage"
        exit(1)

    # Get page title
    title_tag = soup.html.head.title

    # Get episode name
    meta_name = soup.find('meta', {'name':'description'})['content']
    print "Acquiring: {0}".format(meta_name)

    # Find them iframes
    spans = soup.find_all('iframe')
    #print [x for x in spans]

    # Assuming that it is always the first hit
    try:
        vid_link = spans[0].attrs['src']
        logging.debug("Vid_link: {}".format(vid_link))
    except:
        print "Failed scr attribute index 0"
        exit(1)

    # Get the page the iframe refers to
    r = requests.get(vid_link)
    logging.debug("Iframe Ref: {}".format(r))
    logging.debug("Iframe Contents: {}".format(r.content))

    # Load another soup, maybe just one is needed
    soup2 = BeautifulSoup(r.content, "lxml")
    logging.debug("Soup2: {}".format(soup2))

    # To logger, show all
    vidz = soup2.find_all('source')

    # Get that link and print the contents
    try:
        vids = soup2.find_all('source')[0].get('src')
        print "Found the episode link!: {0}".format(vids)
    except IndexError as e:
        print "Could not find the episode link!"
        logging.debug(e)
        exit(1)

    # Get the contents
    fh = urllib2.urlopen(vids)

    # Run the downloader and saver
    download_saver(meta_name, fh)

    print "Done!"

def download_saver(meta_name, fh):
    # Chunk based download, do not save all in memory
    CHUNK = 16 * 1024
    with open('{}'.format(meta_name), 'wb') as code:
        while True:
            data = fh.read(CHUNK)
            if not data: break
            code.write(data)

def bugging_out(debug):
    LEVELS = { 'debug': logging.DEBUG,
               'info' : logging.INFO,
               'warn' : logging.WARNING,
               'crit' : logging.CRITICAL,
             }
    level = LEVELS.get(debug.lower(), logging.NOTSET)
    logging.basicConfig(level=level)
    logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description='Download some files')
    parser.add_argument('-u','--url',metavar='url', required=True,
                        dest='urls', help='url to download from')
    parser.add_argument('-d', dest='debug', help='debug')
    args = parser.parse_args()

    url = args.urls
    debug = args.debug

    return url, debug

def main():

    url, debug = parse_args()

    if debug:
        bugging_out(debug)

    soupify(url)

if __name__ == '__main__':
    main()
