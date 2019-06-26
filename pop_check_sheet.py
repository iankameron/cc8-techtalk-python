import os
import xlrd
from jaconv import z2h
import datetime
from pop_util import getDate, extractData

directory = "data-pop"
x = 0
for filename in os.listdir(directory):
  xlFile = xlrd.open_workbook(directory + "/" + filename)
  sheetList = list(map(lambda x : x.name, xlFile.sheets()))
  # print(sheetList)
  if '5歳階級別人口' in sheetList:
    print("OK")
  else:
    print("NG --- " + filename)
  x = x+ 1
