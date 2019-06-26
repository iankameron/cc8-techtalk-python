import datetime
import calendar

def makeURL(distance, lat, long, startdate, enddate, page):
  return ("https://api.safecast.org/measurements.json?" 
    + "distance=" + str(distance) 
    + "&latitude=" + str(lat) + "&longitude=" + str(long)
    + "&captured_after=" + startdate + "+00%3A00"
    + "&captured_before=" + enddate + "+00%3A00"
    + "&page=" + str(page))

def add_months(sourcedate, months):
  month = sourcedate.month - 1 + months
  year = sourcedate.year + month // 12
  month = month % 12 + 1
  day = min(sourcedate.day, calendar.monthrange(year,month)[1])
  return datetime.date(year, month, day)