# coding: utf8

import requests
import os
import re
from subprocess import call

def tts(text):
    #r = requests.get("http://tts.iiit.ac.in/~kishore/cgi-bin/TTS_telugu.cgi",
    #                 params={'utf8': utf8, 'sel_voice': 'hari_tel_uss'})

    #wav_path = re.search('[a-z]+_\d+.wav', r.text).group()

    #os.system("wget http://tts.iiit.ac.in/~kishore/"+wav_path)
    #os.system("play "+wav_path)
    #os.system("rm "+wav_path)
    call(["./../flite/bin/flite", "-voice", "../flite/voices/cmu_indic_tel_ss.flitevox", "--setf", "duration_stretch=1.3","--setf int_f0_target_mean=145", "-f", text])

if __name__ == '__main__':
	tts(text)