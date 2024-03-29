#! /usr/bin/env python
# coding: utf-8

import subprocess as sp
import os

def main():
    get_tenki = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/tenki/get_tenki.py")
    tenki_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/tenki/tenki.txt")

    speak0_py = os.path.join(os.path.dirname(os.path.abspath(__file__)),"speak0.py")
    wav_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"wav/*.wav")

    sp.call("python3 {0}".format(get_tenki), shell=True)
    sp.call("python3 {0} -i {1}".format(speak0_py, tenki_txt), shell=True)
    sp.call("rm {0}".format(wav_path), shell=True)


if __name__ == '__main__':
    main()
