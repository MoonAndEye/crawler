#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import datetime
import re
import csv
import pandas as pd
import os


target = "http://k-db.com/stocks/"


html = urllib.urlopen(target)
bsObj = BeautifulSoup(html.read())

print(bsObj.h1)
print(bsObj.title)

rawStr = str(bsObj.title)

p = re.compile(r'\d+') #把所有的數字都抓出來

match = p.findall(rawStr) #這個很好用，回傳 list，在這裡 match[0] = year, match[1] = month, match[2] = date
"""
 if match:
    # 得到匹配結果
    print(match.group())
else:
    print("no match!")
"""
print(match)
    

sep = "-"
fileDate = sep.join(match)
print (fileDate)  #這個就是網頁上的日期，然後把他寫入 log 檔，寫一定是寫在最上面
parsingTime = "(" + str(datetime.datetime.today()) + ")"
print (parsingTime)

"""
#第一步是先讀檔，把他讀入 history 裡面，然後新抓的，再把他寫在一開始
"""
writeName = "JpParsingLog" + ".log"
f = open(writeName, 'r')
historyData = f.read()
f.close()

writeSep = "\t"
#writePath = "~/1save/JpStock"


#rawFilePath = os.path.join(writePath, writeName)  #不知道為什麼，他找不到這個 file

logToday = writeSep.join([fileDate,parsingTime])
logToday = historyData + "\n" + logToday

print(logToday)

f = open(writeName, 'w')    #先把他寫到同一個 folder
f.write(logToday)
f.close()
