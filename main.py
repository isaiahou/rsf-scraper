import requests
import os
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gspread
import datetime
import time

service = Service(os.environ.get('CHROMEDRIVER_PATH'))
chrome_options = Options()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=chrome_options)


def parse():
    date = datetime.datetime.now()
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


schedule.every().day.at("07:00").do(execute)
schedule.every().day.at("08:00").do(execute)
schedule.every().day.at("09:00").do(execute)
schedule.every().day.at("10:00").do(execute)
schedule.every().day.at("11:00").do(execute)
schedule.every().day.at("12:00").do(execute)
schedule.every().day.at("13:00").do(execute)
schedule.every().day.at("15:00").do(execute)
schedule.every().day.at("16:00").do(execute)
schedule.every().day.at("17:00").do(execute)
schedule.every().day.at("18:00").do(execute)
schedule.every().day.at("19:00").do(execute)
schedule.every().day.at("20:00").do(execute)
schedule.every().day.at("21:00").do(execute)
schedule.every().day.at("22:00").do(execute)
while True:
    schedule.run_pending()
    time.sleep(.1)
