import requests
from rad_util import makeURL, add_months
import datetime
import math

resolution = .05
adjust = 1 / resolution
startLat = math.floor(36.95 * adjust)
endLat = math.floor(37.95 * adjust)
startLong = math.floor(140.00 * adjust)
endLong = math.floor(141.05 * adjust)

distance = 1000
baseDate = datetime.date(2019,4,1)
numTimeBlocks = 1
timeBlockSize = 3 # in months. 3 is quarterly
pagesPerBlock = 5
starttime = datetime.datetime.now()
print(starttime)
for mnth in range(1, numTimeBlocks + 1):
  startDate = add_months(baseDate, (mnth - 1) * timeBlockSize)
  endDate = add_months(baseDate, (mnth - 1) * timeBlockSize + timeBlockSize)
  start = str(startDate)
  end = str(endDate)
  f = open("data-rad/radiation" + start + ".dat", "w+")
  for lat in range(startLat, endLat + 1):
    for lng in range(startLong, endLong + 1):
      dataSum = 0
      dataCount = 0
      page = 1
      while True:
        urlString = makeURL(distance, lat/adjust, lng/adjust, start, end, page)
        print(lat/adjust, lng/adjust, start, end)
        try:
          response = requests.get(urlString)
          responsejson = response.json()
          if len(responsejson) > 0:
            for data in responsejson:
              if data["unit"] == "cpm":
                dataSum += data["value"]
                dataCount += 1

            if page < pagesPerBlock:
              page = page + 1
            else:
              break
          else:
            break
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("connection failed, retrying")  
        
      if dataCount > 0:
        f.write(",".join([
          start, 
          str(lat/adjust), 
          str(lng/adjust), 
          str(dataSum/dataCount),
          data["unit"]
        ]))
        f.write("\n")
  f.close()



endtime = datetime.datetime.now()
print(endtime)
print(endtime - starttime)
