# coding: utf8
from pydub import AudioSegment
import stt
import tts
from googletrans import Translator
import sys
import os


def main():
    #link = sys.argv[1]
    #os.system('youtube-dl -i --extract-audio --audio-format mp3 --output "test.mp3" '+link)
    translator = Translator()

    song = AudioSegment.from_file("test.m4a", format="mp4")
    i = 0
    while i < len(song):
    sli = song[i:i+15000]
    fname = str(i)+".wav"
        sli.export(fname, format="wav")
        i += 15000
        data = stt.getoutput(fname)
        print(data)
        text = translator.translate(data, src="en", dest="te").text
        tts.tts(utf8=text)

if __name__ == '__main__':
    main()
