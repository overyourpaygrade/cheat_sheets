#!/usr/bin/env python

import time, datetime
import argparse
import json
import requests
import logging
import csv
from pprint import pprint

def main():

    parser = argparse.ArgumentParser(description='Polonix Public Data Display')

    parser.add_argument('-m',dest='mode',action='store',
                        help='Op mode: file, tick, calc or all')

    parser.add_argument('-c',dest='currency',action='store',
                        type=float,help='Current price of the currency in BTC')

    parser.add_argument('-s',dest='shares',action='store',
                        type=int,help='Share amount')

    parser.add_argument('--loop',dest='inf_loop',action='store_true',
                        help='loop mode')

    parser.add_argument('-d','--dump',dest='dump', action='store_true',
                        help='dump mode')

    parser.add_argument('-l','--log',dest='log', help='log mode')


    args = parser.parse_args()

    if not args.mode:
        parser.print_help()
        usage()

    # Ugly logging block
    global logger
    if args.log:
        logger = err_logger(args.log)
        logger.info(args.mode)

    # What to do here
    if args.mode == 'tick':
        loops(args)
    elif args.mode == 'calc':
        calculate(args)
    elif args.mode == 'file':
        analyze(args)
    elif args.mode == 'all':
        q_all()

def usage():
    print '''

            Ex:
            # Analyze csv file w two values
            # Coinname,ShareAmount
            # with optional dump to file mode
            polo_api -m file --dump

            # Calculate coins * value in btc
            polo_api -m calc -s 100 -c 0.01

            # Query all coins and loop (optional)
            polo_api -m tick --loop

            # Query the price of all and convert
            # with some constraints (ignore XMR and USD)
            polo_api -m all

          '''


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


def calculate(args):

    (currency,shares) = (args.currency,args.shares)

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

def excel_dump(all_pairs,coinname,currency,btc_price,val_in_usd,
                last_price,coins,writer):

    basevol = all_pairs[coinname]['baseVolume']
    high24 = all_pairs[coinname]['high24hr']
    highbid = all_pairs[coinname]['highestBid']
    low24 = all_pairs[coinname]['low24hr']
    prcntchg = all_pairs[coinname]['percentChange']
    quotevol = all_pairs[coinname]['quoteVolume']

    list_all = [coinname,basevol,high24,highbid,
                low24,prcntchg,quotevol,currency,
                btc_price,val_in_usd,last_price,
                coins]
    writer.writerow(list_all)


def analyze(args):

    logger = logging.getLogger('__analyze__')

    all_pairs = q_asset_ticker()
    btc_usd = all_pairs['USDT_BTC']['last']

    try:
        with open('asset_list.csv') as fh_csv,\
                open('analysis.csv','ab+') as fh_out:

            writer = csv.writer(fh_out)
            header = ["coinname","basevol","high24","highbid",
                "low24","prcntchg","quotevol","currency","btc_price",
                "val_in_usd","last_price","cointotal",
                datetime.datetime.now()]
            writer.writerow(header)
            asset_list = list(csv.reader(fh_csv))

            print "{:10} {:13} {:12} {:8} {}".format(\
                "Coin","Polo Price","Amount","Dollars", "One")

            for coinname,shares in asset_list:

                currency = float(all_pairs['{}'.format(coinname)]['last'])
                btc_price = int(btc_usd.split('.')[0])
                val_in_usd = (currency * float(shares)) * btc_price
                last_price = all_pairs['{}'.format(coinname)]['last']

                if 'USDT_BTC' in coinname:
                    price_of_one = (currency * 1)
                else:
                    price_of_one = (currency * 1) * btc_price

                print "{:10} {:13} {:12} {:07.2f} {:04.3f}".format(\
                    coinname,last_price,
                    shares, val_in_usd,price_of_one,
                    )

                if args.dump == True:

                    excel_dump(all_pairs,coinname,currency,
                        btc_price,val_in_usd,last_price,
                        shares,writer)

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
