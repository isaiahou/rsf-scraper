import datetime
import time
import pytz


def check_if_in_time():
    date = datetime.datetime.now(pytz.timezone('Europe/London'))
    month = date.strftime("%B")
    day = date.strftime("%A")
    time = date.strftime("%I:%M %p")
    print(month, day, time)
    timestamp = date.time()
    start = datetime.time(12)
    end = datetime.time(22)
    print(start <= timestamp <= end)


check_if_in_time()
