import re

def cleanName(name):
  if name.find("\u3000") != -1:
    return name[name.find("\u3000"):].replace("\u3000", "")
  elif name.find("・") != -1:
    return name[(name.find("・"))+1:]
  else:
    return name

def processCoords (coord):
  coord = coord.replace("x","0")
  digCoord = []
  coordArray =  re.split("[NE′°]+", coord)
  digCoord.append(float(coordArray[1]) + float(coordArray[2]) / 60)
  digCoord.append(float(coordArray[3]) + float(coordArray[4]) / 60)
  return digCoord