from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf-8")

soup = BeautifulSoup(page_content, "html.parser")

ul = soup.find("ul","")

li_list = ul.find_all("li")

itune_list = []
for li in li_list:
    a = li.a
    h3 = li.h3
    h4 = li.h4
    Baihat = h3.string
    Casi = h4.string
    link = url+a["href"]

    itune = OrderedDict({
        "Baihat": Baihat,
        "Casi": Casi,
        "link": link,
    })
    itune_list.append(itune)
pyexcel.save_as(records=itune_list, dest_file_name="Itunes_top_song.xlsx")