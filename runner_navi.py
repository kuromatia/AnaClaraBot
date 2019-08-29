#! /usr/bin/env python
# coding: utf-8

import subprocess as sp
import os

def main():
    get_tenki = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/tenki/get_tenki.py")
    tenki_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/tenki/tenki.txt")

    sp.call("python3 {0}".format(get_tenki), shell=True)
    sp.call("python3 speak0.py -i \"{0}\"".format(tenki_txt), shell=True)


if __name__ == '__main__':
    main()
