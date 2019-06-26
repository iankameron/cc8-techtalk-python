from bs4 import BeautifulSoup as BS
import requests

original_site = requests.get("https://www.pref.fukushima.lg.jp/sec/11045b/15859.html")
original_site.encoding = original_site.apparent_encoding

site_soup = BS(original_site.text, "html.parser")

all_links = site_soup.find_all("a")

for idx, item in enumerate(all_links):
  if str(item.get('href', None)).find("xls") > -1 and str(item.text).find('現在') > -1:
    oneFile = requests.get("https://www.pref.fukushima.lg.jp" + str(item.get('href', None)))
    print(oneFile)
    f = open("data-pop/" + str(item.text) + ".xls", "wb")
    f.write(oneFile.content)
    f.close()
