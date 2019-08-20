#! /usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup
import urllib.request as req
import time
import os


class GetTenki:
    def __init__(self):
        pass

    def get_list(self):
        # base = "https://tenki.jp/forecast/3/17/4620/14150/"
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        data = soup.find_all("li", class_='arxiv-result')

    def main():
        pass


if __name__ == '__main__':
    GetTenki().main()
