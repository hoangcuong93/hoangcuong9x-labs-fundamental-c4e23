from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
#1. connect to the page
url = "https://dantri.com.vn/"
conn = urlopen(url)


#2. dowload the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")
print(page_content)

#with open("dantri.html", "wb") as f:
    #f.write(raw_data)



#3. find ROI region
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul", "ul1 ulnew") # href="" # id =""
# print(ul.prettify())


#4. extract date
li_list = ul.find_all("li")
news_list = []
for li in li_list:
    a = li.h4.a
    tile = a.string
    link = url + a["href"]
    news = OrderedDict({
        "tile": tile,
        "link": link,
    })
    news_list.append(news)
    
    


#5. save data
pyexcel.save_as(records=news_list, dest_file_name="dantri.xls")