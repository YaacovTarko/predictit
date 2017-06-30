#!/usr/bin/env Python3
import requests
import json
import datetime
import time
from pymongo import MongoClient
client = MongoClient() 
db = client.predictit_data
hist = db.historical

url = "https://www.predictit.org/api/marketdata/all/"


while(True):
	start = datetime.datetime.now()
	try:
		ret = requests.get(url, timeout = 10).text
	except Exception:
		sleep(1800)
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

	finish = datetime.datetime.now()
	print("Data Collected at %s" % str(finish) )
	time_elapsed = (finish-start).total_seconds()
	if(time_elapsed < 30):
		time.sleep(30-time_elapsed)