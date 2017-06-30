#!/usr/bin/env Python3
import requests
import json

url = "https://www.predictit.org/api/marketdata/all/"

ret = requests.get(url).text

markets = []

for market in json.loads(ret)["Markets"]:
	for contract in market["Contracts"]:
		if contract["BestBuyYesCost"] is not None and contract["BestSellYesCost"] is not None:
			spread = contract["BestBuyYesCost"]-contract["BestSellYesCost"]
			#print("%s spread = %f" % (market["Name"], spread) )
			markets.append([spread, contract["LongName"]])

markets.sort()
for market in markets:
	print("%s spread = %f" % (market[1], market[0]) )