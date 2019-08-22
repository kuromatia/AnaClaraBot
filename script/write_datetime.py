#! /usr/bin/env python
# coding: utf-8

import re
import datetime
import subprocess as sp


def main():
    today = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    print(today)



if __name__ == '__main__':
    main()
