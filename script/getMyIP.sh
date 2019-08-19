#! /bin/bash

ip a show wlan0 | grep -oP "(?<=inet.)\d{3}[\.\d]*"
