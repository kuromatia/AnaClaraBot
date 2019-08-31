#! /usr/bin/env python
# coding: utf-8

import subprocess as sp
import os
import random
import datetime
import re


def get_time():
    today = datetime.datetime.today().strftime("%m月%d日%H時%M分")
    if re.search("^0", today):
        today = today[1:]
    return(today)

def get_weekday():
    weekday = datetime.date.today().weekday()
    day_name = ["月", "火", "水", "木", "金", "土", "日"]
    return(day_name[weekday])

def get_season():
    month = int(datetime.datetime.today().strftime("%m"))
    if (month == 3 or month == 4 or month == 5):
        pass
    elif (month == 6 or month == 7 or month == 8):
        pass
    elif (month == 9 or month == 10 or month == 11):
        pass
    elif (month == 12 or month == 1 or month == 2):
        pass


def main():
    use_day_info = True

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mono.txt"), "r") as f:
        data = f.read().split("\n")
    data.remove("")
    now = datetime.datetime.today().strftime("%H")

    if (int(now) > 19):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mono_late.txt"), "r") as f:
            data2 = f.read().split("\n")
        data2.remove("")
        data.extend(data2)


    if (use_day_info):
        data.append("現在" + get_time() + "です。")
        data.append("今日は" + get_weekday() + "曜日です。")

    print(data)
    return(0)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"mono_say.txt"), "w") as f:
        f.write(random.choice(data))



if __name__ == '__main__':
    main()
