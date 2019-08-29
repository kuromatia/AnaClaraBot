#! /usr/bin/env python
# coding: utf-8

import subprocess as sp
import os

def main():
    choice_monologue = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/monologue/choice_monologue.py")
    mono_say = os.path.join(os.path.dirname(os.path.abspath(__file__)),"patch/monologue/mono_say.txt")

    speak0_py = os.path.join(os.path.dirname(os.path.abspath(__file__)),"speak0.py")
    wav_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"wav/*.wav")

    sp.call("python3 {0}".format(choice_monologue), shell=True)
    sp.call("python3 {0} -i {1}".format(speak0_py, mono_say), shell=True)
    sp.call("rm {0}".format(wav_path), shell=True)


if __name__ == '__main__':
    main()
