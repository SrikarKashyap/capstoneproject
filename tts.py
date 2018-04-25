# coding: utf8

import requests
import os
import re
from subprocess import call


def tts():
    """
    Convert the telugu text to speech using CMU/Suresh Bazaj flite processor

    Parameters
    ----------
    None
        directly retrieves filenames from system (predefined)

    Returns
    -------
    None
        generates audio file for the telugu text

    TODO
    ----
        better processing model for processing. preferably simulatenous processing and playing.

    """

    """
    FALLBACK/BACKUP method for TTS generation, courtesy Kishore of IIIT Hyderabad

    r = requests.get("http://tts.iiit.ac.in/~kishore/cgi-bin/TTS_telugu.cgi",
                     params={'utf8': utf8, 'sel_voice': 'hari_tel_uss'})

    wav_path = re.search('[a-z]+_\d+.wav', r.text).group()

    os.system("wget http://tts.iiit.ac.in/~kishore/"+wav_path)
    os.system("play "+wav_path)
    os.system("rm "+wav_path)
    """

    print("Entered Text to Speech")
    # call(["./../flite/bin/flite", "-voice", "../flite/voices/cmu_indic_tel_ss.flitevox", "--setf", "duration_stretch=1.3","--setf int_f0_target_mean=145", "../flite/doc/input.txt", "data.wav"])
    os.system("./../flite/bin/flite -voice ../flite/voices/cmu_indic_tel_ss.flitevox --setf duration_stretch=1.15 --setf int_f0_target_mean=145 ../flite/doc/input.txt output.aac")
