import xlrd
from jaconv import z2h
import datetime
from pop_util import getDate, extractData
import os

directory = "data-pop"

allPopData = []
for filename in os.listdir(directory):
  if (filename[0] == "平"):
    print(filename)
    xlFile = xlrd.open_workbook("data-pop/" + filename)
    sheet = xlFile.sheet_by_index(0)
    sheetData = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
    fileDate = getDate(sheetData)
    popData = extractData(sheetData, fileDate)
    allPopData.extend(popData)

f = open("population.dat", "w+")
f.write(str(allPopData))
f.close()