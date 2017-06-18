#-*- coding: utf-8 -*-
import urllib2
import pandas as pd

target = "~/3python/jpStockCrawler/stocks_2017-06-16.csv"

#target = "http://k-db.com/stocks/?download=csv"

#csvFile = urllib2.urlopen(target)
#csvFile1 = csvFile.read()
#s = csvFile1.decode('utf8')
csvFile = pd.read_csv(target)

print csvFile[:10]

#print s