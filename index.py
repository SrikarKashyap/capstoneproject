#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

from pydub import AudioSegment
import stt
import tts
from googletrans import Translator
import sys
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


def extractaudio(filename):
    """
    Extracts audio file from the video link given using ffmpeg

    Parameters
    ----------
    filename: str
        the original filename retrieved from args

    Returns
    -------
    filename: str
        the audio file name

    """
    # print("Entered Extract Audio")
    os.system("""ffmpeg -i """+filename+""" -nostats -loglevel 0 -vn -acodec copy """+filename+""".aac""")
    return str(filename+".aac")


def mutevideo(filename):
    """
    Mute the given video (remove audio track) using ffmpeg

    Parameters
    ----------
    filename: str
        the original filename retrieved from args

    Returns
    -------
    mutedfilename: str
        the video file without audio track

    """
    # print("Entered Mute Video")
    mutedfilename = filename[:len(filename)-4]+".muted"+filename[len(filename)-4:]
    os.system("""ffmpeg -i """+filename+""" -nostats -loglevel 0 -codec copy -an """+mutedfilename)
    return mutedfilename


def cleantext(engtext):
    """
    Clean the text from discrepancies

    Parameters
    ----------
    engtext: str
        the english text retreived from IBM Watson

    Returns
    -------
    engtext: str
        the cleaned and refined text

    TODO
    ----
        better ways to clean and more text to refine

    """
    # print("Entered Clean Text")
    return engtext.replace("%", "").replace("HESITATION", "")


def mergevideoaudio(filename, mutevid):
    """
    Merge the new audio track and muted video using ffmpeg

    Parameters
    ----------
    mutedvid: str
        the name of the muted video to operate on

    Returns
    -------
    None
        Merges through OS system call

    """
    os.system("""ffmpeg -i """+mutevid+""" -nostats -loglevel 0 -i output.aac -shortest -c:v copy -c:a aac -b:a 256k -strict -2 """+filename+""".output.mp4""")


def process(file):
    """
    Core Processing. Get individual audio files, send them to IBM Watson for processing
    Retrieve the file, clean it for discrepancies and translate it to Telugu
    ***USES PARALLEL PROCESSING WITH 15 Threads***

    Parameters
    ----------
    file: str
        the individual file on which to process.

    Returns
    -------
    text: str
        the utf8 telugu text for further TTS generation for each file.

    """
    translator = Translator()
    data = stt.getoutput(file)
    data = cleantext(data)
    # print(data)
    text = translator.translate(data, src="en", dest="te").text
    return text


def cleanup(mutevid, audiofile):
    """
    Garbage cleaning by removing redundant and residual files

    Parameters
    ----------
    mutevid: str
        the file path of muted video which has no use now.
    audiofile: str
        the intermediate audio file generated for processing.

    Returns
    -------
    None
        removes all the intermediate WAV files, audio files and muted video generated.

    """
    os.system("rm *.wav")
    os.system("rm "+mutevid)
    os.system("rm output.aac")
    os.system("rm "+audiofile)
def main(filename):
    """
    main() function of the program.

    Parameters
    ----------
    filename: str
        the original filename retrieved that will be retrieved from sys.args

    Returns
    -------
    None
        partitions audio file, parallel processes them with 15 threads and combines output

    TODO
    ----
        Better parallel processing and queue management. Simulatenous processing and playing preferred

    """
    # filename = sys.argv[1]
    # os.system('youtube-dl -i --extract-audio
    # --audio-format mp3 --output "test.mp3" '+link)
    if filename.split(".")[1] != "mp4":
        return 1
    audiofile = extractaudio(filename)
    # for telugu text storage for conversion later. easier with files than lists
    f = open("/home/srikarkashyap/flite/doc/input.txt", "w")
    # mute the video stream
    mutevid = mutevideo(filename)
    # cleanup of previous outputs to prevent conflicts
    #try:
        #os.system("rm output.mp4")
        #os.system("rm *.wav")
        #os.system("rm *.muted.*")
        #os.system("rm *.aac")
    #except:
    #    pass
    song = AudioSegment.from_file(audiofile, format="aac")
    if len(song) > 480000:
        return 2
    fileparts = []
    i = 0
    # partition the audio file into 15 second segments for faster and easier processing
    while i < len(song):
        name = str(i)+".wav"
        fileparts.append(str(i)+".wav")
        slic = song[i:i+15000]
        slic.export(name, format="wav")
        i += 15000
    # parallel processing using 15 threads by ThreadPool library
    pool = ThreadPool(25)
    results = pool.map(process, fileparts)
    f.write(" ".join(results))
    f.close()
    # perform text to speech synthesis of telugu text
    tts.tts()
    # generate final output video by merging muted video and telugu audio
    mergevideoaudio(filename, mutevid)
    # cleanup tasks including deleting redundant files
    cleanup(mutevid, audiofile)
    # print(results)
    return 0


if __name__ == '__main__':
    main()


