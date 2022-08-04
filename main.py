import requests
from bs4 import BeautifulSoup
import gspread
import datetime

def request():
    


gc = gspread.service_account(filename="creds.json")
sh = gc.open("RSF Crowd Meter Data").sheet1

sh.append_row()