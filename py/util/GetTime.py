import time
import datetime
from util import convert_data


def u_get_current_date():
    currentDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))                    
    return currentDate


def u_get_yesterday_date():
    now_date = datetime.datetime.now()
    yes_date = now_date + datetime.timedelta(days=-1)
    yes_time_nyr = yes_date.strftime('%Y-%m-%d')
    return yes_time_nyr


def u_get_yesterday_timeStamp():
    yesterday_date = u_get_yesterday_date()
    yesterday_start_time = str(int(time.mktime(time.strptime(str(yesterday_date), '%Y-%m-%d'))))
    return yesterday_start_time


def u_get_today_timeStamp():
    return int(time.time())


