#! /usr/bin/env python
# coding: utf-8

import re
import subprocess as sp

class speaker:
    def __init__(self):
        self.script = ""
        self.cmd = ""
        self.output_file_name = ""
        self.output_file_list = ["tenki1.wav", "tenki2.wav", "tenki3.wav", "tenki4.wav", "tenki5.wav", "tenki6.wav", "tenki7.wav"]

    def read_file(self, file_name="script.txt"):
        with open(file_name, "r") as f:
            self.script = f.read()
        return(self.script)

    def write_script(self, input_txt="a", output_file_name="open_jtalk_tmp.wav"):
        self.output_file_name = output_file_name
        self.cmd = "echo '{0}' | open_jtalk -m /usr/share/hts-voice/htsvoice-tohoku-f01/tohoku-f01-neutral.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./{1}".format(input_txt, output_file_name)
        return(self.cmd)

    def call_aplay(self):
        sp.call("aplay {0}".format(self.output_file_name), shell=True)


    def main(self):
        self.read_file("tenki_script.txt")
        self.script = self.script.split("\n")
        self.script.remove("")

        for cnt, i in enumerate(self.script):
            self.write_script(i, self.output_file_list[cnt])
            sp.call(self.cmd, shell=True)

        for i in self.output_file_list:
            sp.call("aplay {0}".format(i), shell=True)


if __name__ == '__main__':
    speaker().main()
