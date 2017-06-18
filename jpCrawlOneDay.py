#-*- coding: utf-8 -*-
import urllib2
import pandas as pd
import datetime
import os

#target = "~/3python/jpStockCrawler/stocks_2017-06-16.csv"



target = "http://k-db.com/stocks/?download=csv"

#csvFile = urllib2.urlopen(target)
#csvFile1 = csvFile.read()
#s = csvFile1.decode('utf8')

chtNameList = ["個股代號", "日文名稱", "交易所在", "開盤", "最高", "最低", "收盤" , "成交株數", "成交金額"]

engNameList = ["StockSymbol", "CompanyName", "StockExchangePlace", "Open", "High", "Low","Close", "Vol" ,"Amount"]
rawFile = pd.read_csv(target, names = engNameList)

rawFile = rawFile[1:]  #一定要把第一行去掉，因為我們加了自己的 header 所以要去掉


print rawFile[:10]  #檢查一下第一行是不是 1301-T

judgeFlag = "1301-T"

test = rawFile["StockSymbol"][1]
#print test

if judgeFlag == test:
    print ("Correct, go on.")
else:
    print ("Something wrong. First item should be 1301-T")

#print s

companyList = rawFile[rawFile.columns[0]]

#q = pd.Series([s])
rawCompanyCsvPath = "~/1save/JpStock/CompanyNameList" 

todayStr = datetime.datetime.today().strftime('%Y-%m-%d')
fileName = "CompanyNameList_" + todayStr + ".csv"

rawFilePath = os.path.join(rawCompanyCsvPath, fileName)

#print s[11:20]

companyList.to_csv(rawFilePath ,index=False , encoding="utf-8")

rawDailyTick = rawFile.copy()

# df.drop(df.columns[[0,1,3]], axis=1, inplace=True)
#ss = rawDailyTick.drop(rawDailyTick.columns[[1,2]], axis=1, inplace=True)

rawDailyTick.pop(engNameList[1])  #用list 砍掉 col 比較安全
rawDailyTick.pop(engNameList[2])  #這兩個 col 會有日文，目前我無法轉掉亂碼

print(rawDailyTick[:10])

rawDailyTickPath = "~/1save/JpStock/RawDailyTick"
dailyTickFileName = "RawDailyTick_" + todayStr + ".csv"

rawFilePath = os.path.join(rawDailyTickPath, dailyTickFileName)

rawDailyTick.to_csv(rawFilePath ,index=False , encoding="utf-8")
