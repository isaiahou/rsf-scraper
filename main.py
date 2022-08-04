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
    print(soup)
    div = soup.find("div", class_ = "styles_fullness__rayxl")
    print(div)
    crowd = div
    result = {'Date': date, "Crowd": crowd}
    return result

# gc = gspread.service_account(filename="creds.json")
# sh = gc.open("RSF Crowd Meter Data").sheet1

# sh.append_row()

data = request()
product = parse(data)
print(product)
