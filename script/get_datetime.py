#! /usr/bin/env python
# coding: utf-8

import re
import datetime

def main():
    today = datetime.datetime.today().strftime("%m月%d日%H時%M分")
    if re.search("^0", today):
        today = today[1:]

    with open("current_time.txt", "w") as f:
        f.write("現在時刻は"+today+"です。")


if __name__ == '__main__':
    main()
