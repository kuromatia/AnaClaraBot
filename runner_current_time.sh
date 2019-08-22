#! /bin/bash

python3 /home/pi/AnaClaraBot/script/get_datetime.py
python3 /home/pi/AnaClaraBot/speak0.py -i "/home/pi/AnaClaraBot/current_time.txt"
rm /home/pi/AnaClaraBot/wav/*.wav
