#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup


urls = ["https://en.wikipedia.org/wiki/List_of_Black_Sails_episodes", 
        "https://en.wikipedia.org/wiki/List_of_Suits_episodes",
        "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
       ]

for url in urls:

    try:
        response = urllib2.urlopen(url)
    except:
        raise
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    
    titleTag = soup.html.head.title
    
    print(titleTag.text)
    
    # Get title 
    for lel in soup.select('td[class="summary"]'):
        print('{}'.format(lel.text.replace('"','')))

