import requests
from bs4 import BeautifulSoup
import gspread
import datetime


def request():
    source = requests.get(
        "https://recsports.berkeley.edu/rsf-weight-room-crowd-meter/")
    soup = BeautifulSoup(source.content, "html.parser")
    return soup


def parse(soup):
    date = datetime.datetime.now()
    div = soup.find(
        "div", class_="styles_main__3Ul1n styles_sidebarOpen__1t7th")
    crowd = div.span.text
    result = {'Date': date, "Crowd": crowd}
    return result

# gc = gspread.service_account(filename="creds.json")
# sh = gc.open("RSF Crowd Meter Data").sheet1

# sh.append_row()


data = request()
product = parse(data)
print(product)
