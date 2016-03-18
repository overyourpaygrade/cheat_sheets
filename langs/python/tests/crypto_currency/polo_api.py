#!/usr/bin/env python

import time
import krakenex
import argparse
import json
import requests
import logging
import csv
from pprint import pprint

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

    parser.add_argument('--loop',dest='inf_loop',action='store_true',
                        help='loop mode')

    parser.add_argument('--log',dest='log', help='log mode')

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

    # Ugly logging block
    global logger
    logger = err_logger(args.log)
    logger.info(args.mode)

    # What to do here
    if args.mode == 'query':
        loops(krak_conn,ticker_vals,args)
    elif args.mode == 'req':
        q_asset_pairs()
    elif args.mode == 'calc':
        calculate(krak_conn,args.currency,args.shares)
    elif args.mode == 'file':
        analyze(krak_conn)
    elif args.mode == 'tick':
        q_asset_ticker()
    elif args.mode == 'all':
        q_all()

def err_logger(log):

    LEVELS = { 'debug':logging.DEBUG,
                'info':logging.INFO,
                'warning':logging.WARNING,
                'error':logging.ERROR,
                'critical':logging.CRITICAL,
                }

    level_name = log
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logger = logging.getLogger(__name__)

    return logger


def calculate(krak_conn,currency,shares):

    xbtc2usd = krak_conn.query_public('Ticker', {'pair':'XXBTZUSD'})
    btc = xbtc2usd['result']['XXBTZUSD']['a'][0].split('.')[0]

    calc_r = (currency * shares) * int(btc)

    print "Price in USD: ", calc_r


def q_asset_ticker():

    logger = logging.getLogger('q_asset_ticker')

    url = 'https://poloniex.com/public?command=returnTicker'

    r = requests.get(url)

    pairs = json.loads(r.text)

    logger.debug('Asset TPL: {}'.format(pairs))

    return pairs


def q_asset_pairs():

    logger = logging.getLogger('q_asset_pairs')

    url = "https://api.kraken.com/0/public/AssetPairs"

    r = requests.get(url)

    pairs = json.loads(r.text)

    pprint(pairs)

def analyze(krak_conn):

    logger = logging.getLogger('__analyze__')

    all_pairs = q_asset_ticker()
    btc_usd = all_pairs['USDT_BTC']['last']


    with open('asset_list.csv') as fh_csv:

        asset_list = list(csv.reader(fh_csv))

        print "{:10} {:13} {:12} {}".format(\
            "Coin","Polo Price","Amount","Dollars")

        for coinname,shares in asset_list:

            currency = float(all_pairs['{}'.format(coinname)]['last'])
            btc_price = int(btc_usd.split('.')[0])
            val_in_usd = (currency * float(shares)) * btc_price

            print "{:10} {:13} {:12} {:04.2f}".format(\
                coinname,all_pairs['{}'.format(coinname)]['last'],
                shares, val_in_usd
                )

def q_all():

    logger = logging.getLogger('__qall__')

    all_pairs = q_asset_ticker()
    btc_usd = all_pairs['USDT_BTC']['last']
    btc_price = int(btc_usd.split('.')[0])

    for k in all_pairs:

        if 'USD' in k: continue
        if 'XMR' in k: continue

        currency = all_pairs[k]['last']
        val_in_usd = float(currency) * int(btc_price)

        print "{:10} {:13} {:04.2f}".format(k,currency,val_in_usd)


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
