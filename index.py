# coding: utf8
from pydub import AudioSegment
import stt
import tts
from googletrans import Translator
import sys
import os
import sys
from subprocess import run
import subprocess

def extractaudio(filename):
    print("Entered Extract Audio")
    os.system("""ffmpeg -i """+filename+""" -vn -acodec copy """+filename+""".aac""")
    return str(filename+".aac")


def mutevideo(filename):
    print("Entered Mute Video")
    mutedfilename = filename[:len(filename)-4]+".muted"+filename[len(filename)-4:]
    os.system("""ffmpeg -i """+filename+""" -codec copy -an """+mutedfilename)
    return mutedfilename

def cleantext(engtext):
    print("Entered Clean Text")
    return engtext.replace("%", "").replace("HESITATION", "")

def mergevideoaudio(mutevid):
    os.system("""ffmpeg -i """+mutevid+""" -i output.aac -shortest -c:v copy -c:a aac -b:a 256k -strict -2 final.mp4""")
    #os.system("""ffmpeg -i """+mutevid+""" -i output.aac -shortest -c:v copy -b:a 256k final.mp4""")

def main():
    filename = sys.argv[1]
    # os.system('youtube-dl -i --extract-audio --audio-format mp3 --output "test.mp3" '+link)
    audiofile = extractaudio(filename)
    f = open("/home/srikarkashyap/flite/doc/input.txt", "w")
    mutevid = mutevideo(filename)
    translator = Translator()
    song = AudioSegment.from_file(audiofile, format="aac")
    i = 0
    while i < len(song):
        slic = song[i:i+15000]
        fname = str(i)+".wav"
        slic.export(fname, format="wav")
        i += 15000
        data = stt.getoutput(fname)
        data = cleantext(data)
        print(data)
        text = translator.translate(data, src="en", dest="te").text
        f.write(text)
        #tts.tts(text)
        #f.close()
    #run(["./../flite/bin/flite", "-voice", "../flite/voices/cmu_indic_tel_ss.flitevox", "--setf", "duration_stretch=1.3","--setf int_f0_target_mean=145", "../flite/doc/input.txt", "output.wav"], stdout=subprocess.PIPE)
    f.close()
    run(["sh","generateoutput.sh"])
    #os.system("./../flite/bin/flite -voice ../flite/voices/cmu_indic_tel_ss.flitevox --setf duration_stretch=1.3 --setf int_f0_target_mean=145 ../flite/doc/input.txt data.wav")
    mergevideoaudio(mutevid)
    #pid = subprocess.Popen([sys.executable, "generateoutput.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

if __name__ == '__main__':
    main()
