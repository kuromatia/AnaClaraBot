#! /usr/bin/env python
# coding: utf-8

import re
import datetime
import subprocess as sp


def main():
    today = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
    sp.call("date -s {0}".format(today), shell=True)



if __name__ == '__main__':
    main()
