#!/usr/bin/env python

import pprint

dct = {
    'title': {
        '1': ['one', 'two', 'three'],
        '2': ['four','five','six'],
    },
    'genre': {
        'dance': ['bing','bong'],
        'tech': ['bang','bing'],
    },
    'album': {
        'something': ['oneone','twotwo'],
        'boomboom': ['threethree','threethree'],
    }
}

#print pprint.pprint(dct)

host = dct.get('title')
print host['1'][0]
