from bs4 import BeautifulSoup as BS
import requests
from latlong_util import cleanName, processCoords

original_site = requests.get("http://www.gero3p.sakura.ne.jp/files/jisa/fukusima.html")
original_site.encoding = original_site.apparent_encoding
original_site.text

site_soup = BS(original_site.text, "html.parser")

# print(site_soup.table)

allTables = site_soup.find_all("table")

printed = 0
printedHowMany = 2
cityData = []
latLongData = []
for table in allTables:
  allRows = table.find_all("tr")
  for thisRow in allRows:
    headercols = thisRow.find_all("th")
    datacols = thisRow.find_all("td")
    if len(datacols) == 0:
      datacols
      # print("header----------------------")
    elif len(headercols) == 1:
      if datacols[0].text == "":
        cityData.append(cleanName(headercols[0].text))
        latLongData.append(processCoords(datacols[3].text))
      else:
        cityData.append(cleanName(datacols[0].text))
        latLongData.append(processCoords(datacols[3].text))
    else:
      cityData.append(cleanName(datacols[0].text))
      latLongData.append(processCoords(datacols[3].text))

outputFile = open("data-latlong/latLong.dat", "w+")
outputFile.write(str(cityData))
outputFile.write(str(latLongData))

