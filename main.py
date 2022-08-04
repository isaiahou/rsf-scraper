import requests
import os
import schedule
import gspread
import datetime
import time
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(os.environ.get('CHROMEDRIVER_PATH'))
chrome_options = Options()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=chrome_options)


def parse():
    date = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
    url = "https://safe.density.io/#/displays/dsp_956223069054042646?token=shr_o69HxjQ0BYrY2FPD9HxdirhJYcFDCeRolEd744Uj88e"
    driver.get(url)
    attempts = 0
    while attempts < 3:
        try:
            element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/span"))).text.removesuffix("% Full")
            result = {'Date': date, "Crowd": element}
            return result
        except:
            attempts += 1
            element = "There was an error"
            result = {'Date': date, "Crowd": element}
    return result


def output(info):
    gc = gspread.service_account(filename="creds.json")
    sh = gc.open("RSF Crowd Meter Data").sheet1
    sh.append_row([str(info['Date']), str(info['Crowd'])])


def execute():
    info = parse()
    output(info)

schedule.every().hour.at(":00").do(execute)
schedule.every().hour.at(":30").do(execute)
while True:
    schedule.run_pending()
    time.sleep(.1)
