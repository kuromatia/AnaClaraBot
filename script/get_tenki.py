#! /usr/bin/env python3
# coding: utf-8

from bs4 import BeautifulSoup
import urllib
import urllib.request
import re


class GetTenki:
    def __init__(self):
        pass

    def get_list(self, url="https://tenki.jp/forecast/3/17/4620/14150/"):
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, "html.parser")
        data = soup.find_all("section", class_='today-weather')
        for i in data:
            day = i.find("h3", class_='left-style').text
            tenki = i.find("p", class_='weather-telop').text
            max_temp = i.find("dd", class_='high-temp temp').text
            low_temp = i.find("dd", class_='low-temp temp').text
            rain = i.find("tr", class_='rain-probability').text

        youbi  = re.search("(?<=\().(?=\))", day).group()
        day = re.search("\d.*日", day).group()
        max_temp = re.search("\d*", max_temp).group()
        low_temp = re.search("\d*", low_temp).group()
        rain = re.findall("\d*(?=%)", rain)
        rain = max(rain)

        if re.search("^0",day):
            day = day[1:]

        # print(day)
        # print(youbi)
        # print(tenki)
        # print(max_temp)
        # print(low_temp)
        # print(rain)

        result_txt = "今日は" + day + youbi +  "曜日です。\n"
        result_txt2 = "天気は" + tenki + "です。\n" + "最高気温は" + max_temp + "度\n" + "最低気温は" + low_temp + "度\n" +  "降水確率は" + rain + "パーセントです。\n"
        greeting = "おはようございます。\n今日も1日頑張りましょう。\n"

        with open("tenki_script.txt", "w") as f:
            f.write(greeting)
            f.write(result_txt)
            f.write(result_txt2)

    def main(self):
        self.get_list()


if __name__ == '__main__':
    GetTenki().main()
