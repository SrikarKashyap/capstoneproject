# coding: utf8

import requests
import os
import re


def tts(utf8):
    r = requests.get("http://tts.iiit.ac.in/~kishore/cgi-bin/TTS_telugu.cgi",
                     params={'utf8': utf8, 'sel_voice': 'hari_tel_uss'})

    wav_path = re.search('[a-z]+_\d+.wav', r.text).group()

    os.system("wget http://tts.iiit.ac.in/~kishore/"+wav_path)
    os.system("play "+wav_path)
    os.system("rm "+wav_path)
