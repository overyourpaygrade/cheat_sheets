#!/usr/bin/env python

import time, datetime, sys
import json
import requests
import logging
import csv
from pprint import pprint


class poloniexAPI(object):

    def __init__(self,log=False):

        if log == True:
            self.logger = self.err_logger(log)

        self.all_pairs = self.q_asset_ticker()


    def showdoc(self):
        print '''

        # Instantiate with logging or not
        api = poloniexAPI(log='info')
        api = poloniexAPI()

        # Calculate coins * value in btc
        api.calculate(coins=100,value=0.0003)

        # Query asset pairs and information on all, pretty print
        api.q_asset_pairs()

        # Query the price of all and convert
        # with some constraints (ignore XMR INDEX and USD)
        api.q_all()

        # Display all values and information on each pair
        # Loop optional
        api.loops(inf_loop=True)
        api.loops()

        # Analyze csv file w two values
        # Coinname,ShareAmount (BTC_SYS,100)
        # with optional dump to file mode
        api.analyze()
        api.analyze(dump=True)

        # Show usage
        api.showdoc()

              '''
        exit(1)


    def q_asset_ticker(self):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

        url = 'https://poloniex.com/public?command=returnTicker'

        r = requests.get(url)

        pairs = json.loads(r.text)

        self.logger.debug('Asset TPL: {}'.format(pairs))

        return pairs


    @staticmethod
    def err_logger(log=False):

        LEVELS = { 'debug':logging.DEBUG,
                    'info':logging.INFO,
                    'warning':logging.WARNING,
                    'error':logging.ERROR,
                    'critical':logging.CRITICAL,
                    }

        logging.getLogger("requests").setLevel(logging.WARNING)

        if log == True:
            level_name = log
            level = LEVELS.get(level_name, logging.NOTSET)
            logging.basicConfig(level=level)
            logger = logging.getLogger(sys._getframe().f_code.co_name)
            return logger
        else:
            logging.basicConfig(level=logging.NOTSET)


    def calculate(self,coins,value):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)
        self.logger.info('{} {}'.format(coins,value))

        btc = self.all_pairs['USDT_BTC']['last'].split('.')[0]

        calc_r = (value * coins) * int(btc)

        print "\nPrice in USD: {}  Current BTCUSD: {}\n".format(calc_r,btc)


    def q_asset_pairs(self):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

        url = "https://api.kraken.com/0/public/AssetPairs"

        r = requests.get(url)

        pairs = json.loads(r.text)

        pprint(pairs)


    def q_all(self):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

        btc_usd = self.all_pairs['USDT_BTC']['last']
        btc_price = int(btc_usd.split('.')[0])

        for k in self.all_pairs:

            # Find a better way to handle these!
            if 'USD' in k: continue
            if 'XMR' in k: continue
            if 'INDEX' in k: continue

            currency = self.all_pairs[k]['last']
            val_in_usd = float(currency) * int(btc_price)

            print "{:10} {:13} {:04.2f}".format(k,currency,val_in_usd)


    def loops(self,inf_loop=False):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

        all_pairs = self.all_pairs

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

                if inf_loop == False:
                    exit(0)

                time.sleep(10)

            except:
                exit(1)

    def excel_dump(self,all_pairs,coinname,currency,btc_price,val_in_usd,
                    last_price,coins,writer):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

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


    def analyze(self,dump=False):

        self.logger = logging.getLogger(sys._getframe().f_code.co_name)

        all_pairs = self.all_pairs
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

                for coinname,coins in asset_list:

                    currency = float(all_pairs['{}'.format(coinname)]['last'])
                    btc_price = int(btc_usd.split('.')[0])
                    val_in_usd = (currency * float(coins)) * btc_price
                    last_price = all_pairs['{}'.format(coinname)]['last']

                    if 'USDT_BTC' in coinname:
                        price_of_one = (currency * 1)
                    else:
                        price_of_one = (currency * 1) * btc_price

                    print "{:10} {:13} {:12} {:07.2f} {:04.3f}".format(\
                        coinname,last_price,
                        coins,val_in_usd,price_of_one,
                        )

                    if dump == True:
                        self.excel_dump(all_pairs,coinname,currency,
                            btc_price,val_in_usd,last_price,
                            coins,writer)

        except KeyboardInterrupt:
            exit(1)



api = poloniexAPI()
#api = poloniexAPI(log='info')

#api.calculate(coins=100,value=0.0003)

#api.q_asset_pairs()

#api.q_all()

#api.loops(inf_loop=True)
#api.loops()

#api.analyze()
#api.analyze(dump=True)

#api.showdoc()
