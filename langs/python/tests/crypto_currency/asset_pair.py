#!/usr/bin/env python

import requests
import json
from pprint import pprint

url = "https://api.kraken.com/0/public/AssetPairs"

r = requests.get(url)

pairs = json.loads(r.text)

pprint(pairs)
