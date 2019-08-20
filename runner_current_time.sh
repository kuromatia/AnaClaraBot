#! /bin/bash

python3 script/get_datetime.py
python3 speak0.py -i "current_time.txt"
rm ./wav/*.wav
