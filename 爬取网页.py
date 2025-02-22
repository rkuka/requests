import urllib.request
import time
from bs4 import BeautifulSoup
url = 'https://www.cnblogs.com'
respone = urllib.request.urlopen(url)
htmlcontent = respone.read().decode('utf-8')
soup = BeautifulSoup(htmlcontent,"html.parser")
editorPick = soup.find("a",attrs={"id":"editor_pick_lnk"})
contenttext = soup.find("a", attrs={"id":"editor_pick_lnk"}).text
contenttext = soup.find("div",attrs={'class':'card headline'}).text
print(contenttext)
time.sleep(30)