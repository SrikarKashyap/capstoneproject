# coding: utf8
from pydub import AudioSegment
import stt
import tts
from googletrans import Translator
import sys
import os
import sys

_author_ = "Srikar Kashyap Pulipaka"

def main():
    #link = sys.argv[1]
    #os.system('youtube-dl -i --extract-audio --audio-format mp3 --output "test.mp3" '+link)
    translator = Translator()
    song = AudioSegment.from_file("firstprinciples.aac", format="aac")
    i = 0
    outputbuff = []
    while i < len(song):
        slic = song[i:i+15000]
        fname = str(i)+".wav"
        slic.export(fname, format="wav")
        i += 15000
        data = stt.getoutput(fname)
        print(data)
        text = translator.translate(data, src="en", dest="te").text
        f = open("/home/srikarkashyap/flite/doc/input.txt","a")
        f.write(text)   
        outputbuff.append(str(text))
        tts.tts(text)
        #f.close()

if __name__ == '__main__':
    main()
