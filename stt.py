#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='2e1634da-c1c3-441d-b31e-40341d48ebd9',
    password='2pNntsBzU0IS',
)


def getoutput(fname):
    """
    Generate English Text from Speech using IBM Watson STT Engine

    Parameters
    ----------
    fname: str
        the individual file to process on

    Returns
    -------
    text: str
        the transcribed text from the audio clip in english

    """
    #print("Entered Speech to Text")
    with open(join(dirname(__file__), fname),
              'rb') as audio_file:
        recdata = speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            word_confidence=True)
        return recdata["results"][0]["alternatives"][0]["transcript"]
