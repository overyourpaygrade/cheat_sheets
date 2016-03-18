#!/usr/bin/env python

import time
import argparse
import json
import requests
import logging
import csv

def main():

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
    if args.log:
        logger = err_logger(args.log)
        logger.info(args.mode)

    # What to do here
    if args.mode == 'query':
        loops(args)
    elif args.mode == 'req':
        q_asset_pairs()
    elif args.mode == 'calc':
        calculate(args.currency,args.shares)
    elif args.mode == 'file':
        analyze()
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

    if log:
        level_name = log
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level)
        logging.getLogger("requests").setLevel(logging.WARNING)
        logger = logging.getLogger(__name__)
    else:
        logging.basicConfig(level=logging.NOTSET)

    return logger


def calculate(currency,shares):

    all_pairs = q_asset_ticker()

    btc = all_pairs['USDT_BTC']['last'].split('.')[0]

    calc_r = (currency * shares) * int(btc)

    print "\nPrice in USD: {}  Current BTCUSD: {}\n".format(calc_r,btc)


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

def analyze():

    logger = logging.getLogger('__analyze__')

    all_pairs = q_asset_ticker()
    btc_usd = all_pairs['USDT_BTC']['last']

    try:
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

    except KeyboardInterrupt:
        exit(1)

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


def loops(args):

    logger = logging.getLogger('__loops__')

    all_pairs = q_asset_ticker()

    while True:
        try:

            fmt = "{:10} {:13} {:13} {:13} {:13} {:13} {:13} {:10}"

            for k in all_pairs:

                basevol = all_pairs[k]['baseVolume']
                high24 = all_pairs[k]['high24hr']
                highbid = all_pairs[k]['highestBid']
                last = all_pairs[k]['last']
                low24 = all_pairs[k]['low24hr']
                prcntchg = all_pairs[k]['percentChange']
                quotevol = all_pairs[k]['quoteVolume']

                print fmt.format(
                                k, basevol, high24,highbid,
                                last,low24,prcntchg,quotevol,
                                )

            if args.inf_loop == False:
                exit(0)

            time.sleep(10)

        except:
            exit(1)

if __name__ == '__main__':

    main()
