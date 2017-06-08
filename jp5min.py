# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


CSV_URL = 'http://k-db.com/stocks/8306-T/5m?download=csv'


import requests
import csv
import os

temp_file_name = 'temp_csv.csv'
url = 'http://k-db.com/stocks/8306-T/5m?download=csv'
download = requests.get(url)

with open(temp_file_name, 'w') as temp_file:
    temp_file.writelines(download.content)

with open(temp_file_name, 'rU') as temp_file:
    csv_reader = csv.reader(temp_file, dialect=csv.excel_tab)
    for line in csv_reader:
        print line

# delete the temp file after process
os.remove(temp_file_name)
