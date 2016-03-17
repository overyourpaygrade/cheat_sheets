#!/usr/bin/env python

import time
import krakenex
import argparse
import json
import requests
import logging
from pprint import pprint

'''
a = ask array(<price>, <whole lot volume>, <lot volume>),
b = bid array(<price>, <whole lot volume>, <lot volume>),
Sell:
btc2usd['result']['XXBTZUSD']['a'][0]
Buy:
btc2usd['result']['XXBTZUSD']['b'][0]

'''

def main():

    try:
        krak_conn = krakenex.API()
    except:
        print "Could not connect"
        exit(1)

    parser = argparse.ArgumentParser(description='Polonix Public Data Display')

    parser.add_argument('-m',dest='mode',action='store',
                        help='Op mode: Loop, Single, or Asset Pair')

    parser.add_argument('-c',dest='currency',action='store',
                        type=float,help='Current price of the currency in BTC')

    parser.add_argument('-s',dest='shares',action='store',
                        type=int,help='Share amount')

    parser.add_argument('-l',dest='inf_loop',action='store_true',
                        help='loop mode')

    parser.add_argument('-d',dest='debug',action='store_true',
                        help='debug mode')
    args = parser.parse_args()

    supported_asset_pairs = [
        'XETHXXBT', 'XETHZCAD', 'XETHZEUR', 'XETHZGBP', 'XETHZJPY', 'XETHZUSD',
        'XLTCZCAD', 'XLTCZEUR', 'XLTCZUSD', 'XXBTXLTC', 'XXBTXNMC', 'XXBTXXDG',
        'XXBTXXLM', 'XXBTXXRP', 'XXBTZCAD', 'XXBTZEUR', 'XXBTZGBP', 'XXBTZJPY',
        'XXBTZUSD', 'XXBTZJPY.d', 'XXBTZGBP.d', 'XXBTZEUR.d', 'XXBTZCAD.d',
        'XXBTZUSD.d',
        ]

    ticker_vals = { 'a' : 'ask array',
                    'b' : 'bid array',
    }

    logging.basicConfig(level=logging.INFO)
    logger1 = logging.getLogger('')
    logger1.info(args.mode)

    if args.mode == 'query':
        loops(krak_conn,ticker_vals,args)
    elif args.mode == 'req':
        q_asset_pairs()
    elif args.mode == 'calc':
        calculate(krak_conn,args.currency,args.shares)

def calculate(krak_conn,currency,shares):

    xbtc2usd = krak_conn.query_public('Ticker', {'pair':'XXBTZUSD'})
    btc = xbtc2usd['result']['XXBTZUSD']['a'][0].split('.')[0]

    calc_r = (currency * shares) * int(btc)

    print "Price in USD: ", calc_r


def q_asset_ticker(krak_conn):

    xbtc2usd = krak_conn.query_public('Ticker', {'pair':'XXBTZUSD'})
    xeth2usd = krak_conn.query_public('Ticker', {'pair':'XETHZUSD'})
    logger1.debug('Asset TPL: {}'.format(asset_tpl))

    return xbtc2usd, xeth2usd


def q_asset_pairs():

    url = "https://api.kraken.com/0/public/AssetPairs"

    r = requests.get(url)

    pairs = json.loads(r.text)

    pprint(pairs)


def loops(krak_conn,ticker_vals,args):

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

            if args.inf_loop == False:
                exit(0)

            time.sleep(10)

        except:
            exit(1)

if __name__ == '__main__':

    main()
