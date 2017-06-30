#!/usr/bin/env Python3
import requests
import json
import datetime
from pymongo import MongoClient
client = MongoClient() 
db = client.predictit_data
hist = db.historical

url = "https://www.predictit.org/api/marketdata/all/"

ret = requests.get(url).text

for market in json.loads(ret)["Markets"]:
	for contract in market["Contracts"]:
		entry = { "name" : contract["LongName"],
				"LastTradePrice" : contract["LastTradePrice"],
				"BestBuyYesCost" : contract["BestBuyYesCost"],
				"BestBuyNoCost" : contract["BestBuyNoCost"],
				"BestSellYesCost" : contract["BestSellYesCost"],
				"BestSellNoCost" : contract["BestSellNoCost"],
				"LastClosePrice" : contract["LastClosePrice"],
				"Time" : str(datetime.datetime.now())
		}
		post_id = hist.insert_one(entry)
		#entry['']

print("Data Collected at %s" % str(datetime.datetime.now()) )