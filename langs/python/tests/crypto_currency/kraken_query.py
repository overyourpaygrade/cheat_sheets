#!/usr/bin/env python

from pprint import pprint
import time
import krakenex

krak_conn = krakenex.API()

'''
a = ask array(<price>, <whole lot volume>, <lot volume>),
b = bid array(<price>, <whole lot volume>, <lot volume>),
Sell:
btc2usd['result']['XXBTZUSD']['a'][0]
Buy:
btc2usd['result']['XXBTZUSD']['b'][0]

'''

ticker_vals = { 'a' : 'ask array',
                'b' : 'bid array',
}

while True:
    try:

        xbtc2usd = krak_conn.query_public('Ticker', {'pair':'XXBTZUSD'})
        xeth2usd = krak_conn.query_public('Ticker', {'pair':'XETHZUSD'})

        btc2usd_ask = xbtc2usd['result']['XXBTZUSD']['a'][0]
        btc2usd_bid = xbtc2usd['result']['XXBTZUSD']['b'][0]

        eth2usd_ask = xeth2usd['result']['XETHZUSD']['a'][0]
        eth2usd_bid = xeth2usd['result']['XETHZUSD']['b'][0]

        print
        print "BTC2USD ASK: {} -- ETH2USD ASK: {}".format(\
            btc2usd_ask,eth2usd_ask)
        print "BTC2USD BID: {} -- ETH2USD BID: {}".format(\
            btc2usd_bid,eth2usd_bid)
        print

        time.sleep(10)

    except:
        exit(1)


