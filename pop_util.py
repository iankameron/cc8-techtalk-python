from jaconv import z2h
import datetime


def getDate(matrix):
  westernDate = ""
  colCounter = 0
  while westernDate == "":
    if matrix[0][colCounter].find("平成") != -1:
      hankaku = z2h(matrix[0][colCounter], digit=True)
      heisei = hankaku.find("平成")
      nen = hankaku.find("年", heisei)
      gatsu = hankaku.find("月", heisei)
      nichi = hankaku.find("日", heisei)
      y = int(hankaku[(heisei+2):nen]) + 1988
      m = int(hankaku[(nen+1):gatsu])
      d = int(hankaku[(gatsu+1):nichi])
      westernDate = datetime.datetime(y, m, d)
    colCounter = colCounter + 1
  return str(westernDate)

def extractData(matrix, date):
  popData = []
  cityTypes = ["市","町","村"]
  # find starting point
  rowCounter = 1
  while matrix[rowCounter][0].find("福") == -1:
    rowCounter = rowCounter + 1
  while rowCounter <= len(matrix) - 1 and len(matrix[rowCounter][0]) > 0:
    # print(matrix[rowCounter][0])
    if matrix[rowCounter][0][-1] in cityTypes:
      cityName = matrix[rowCounter][0].replace("　","")
      if matrix[rowCounter][1] == "-":
        totalPopulation = 0
      else:
        totalPopulation = int(matrix[rowCounter][1])
      popData.append([date, cityName, totalPopulation])
    rowCounter = rowCounter + 1
  return popData
