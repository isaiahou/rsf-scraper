import requests
from bs4 import BeautifulSoup
import gspread
import datetime
import time

url = "https://recsports.berkeley.edu/rsf-weight-room-crowd-meter/"

def request():
    source = requests.get(url, "html.parser")
    soup = BeautifulSoup(source, "lxml")
    return soup


def parse(soup):
    date = datetime.datetime.now()
    div = soup.find_all("div",  string="% Full")
    # for item in div:
    #     x = item.find('span')
    #     if x:
    #         print(x.text.strip())
    crowd = div
    result = {'Date': date, "Crowd": crowd}
    return result

# gc = gspread.service_account(filename="creds.json")
# sh = gc.open("RSF Crowd Meter Data").sheet1

# sh.append_row()


data = request()
product = parse(data)
print(product)
driver.close()
