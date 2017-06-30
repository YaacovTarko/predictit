#!/usr/bin/env Python3
import requests
import json

url = "https://www.predictit.org/api/marketdata/all/"

ret = requests.get(url).text

markets = []

for market in json.loads(ret)["Markets"]:
	contracts = market["Contracts"][0]
	if contracts["BestBuyYesCost"] is not None and contracts["BestSellYesCost"] is not None:
		spread = contracts["BestBuyYesCost"]-contracts["BestSellYesCost"]
		#print("%s spread = %f" % (market["Name"], spread) )
		markets.append([spread, market["Name"]])

markets.sort()
for market in markets:
	print("%s spread = %f" % (market[1], market[0]) )