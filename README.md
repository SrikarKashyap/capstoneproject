# English to Telugu Video Translator
### About this project
Initial version was developed as part of UC Berkeley Open Innovation Hackathon, India - 2017 (Winner project in Communications vertical) and later underwent various improvements as a part of major project during our undergrad. This application mainly focuses on translation of English videos into Telugu. 

### Overview
In spite of many languages being spoken in India, it is difficult for the people to understand foreign languages like English, Spanish, Italian, etc. The recognition and synthesis of speech are prominent emerging technologies in natural language processing and communication domains. This paper aims to leverage the open source applications of these technologies, machine translation, text-to-speech system (TTS), and speech-to-text system (STT) to convert available online resources to Indian languages. This application takes an English language video as an input and separates the audio
from video. It then divides the audio file into several smaller
chunks based on the timestamps. These audio chunks are then
individually converted into text using IBM Watson’s speech-to-
text (STT) module. The obtained text chunks are then
concatenated and passed to Google’s machine translate API for
conversion to the requested Indian language. After this
translation, a TTS system is required to convert the text into
the desired audio output. Not many open source TTS systems
are available for Indian regional languages. One such available
application is the flite engine (a lighter version of Festival
engine developed by Prof. Alan Black at Carnegie Mellon
University (CMU)). This flite engine is used as TTS for
generating audio from translated text. This application is beneficial to visually impaired
people as well as individuals who are not capable of reading
text to acquire knowledge in their native language. In future,
this application aims to achieve ubiquitous communication
enabling people of different regions to communicate with each
other breaking the language barriers.

### Technologies & APIs used
- ffmpeg, pydub and other libraries for raw video/audio processing and segmentation.
- IBM Watson, Google Translate APIs for Speech-to-Text & translation.
- [CMU Festival (flite)](https://github.com/festvox/flite) for Telugu Text-to-Speech.

![apis](https://github.com/chaitanyakasaraneni/capstoneproject/blob/master/images/api.PNG "APIs used")

### Work-flow of the project
The project development involved three stages.
 - Audio extraction from video
 - Processing the threads parallelly
 - Text-to-Speech and merging
![stages](https://github.com/chaitanyakasaraneni/capstoneproject/blob/master/images/stage.PNG "Work flow")

### Installation and working
Clone the repository by using the following command
```
git clone https://github.com/chaitanyakasaraneni/capstoneproject.git
```
Then headover to the [CMU's flite repo](https://github.com/festvox/flite) and clone that using:
```
git clone http://github.com/festvox/flite
```
After cloning the repo, use the following commands to install the flite engine:
```
cd flite
./configure
make
make get_voices
```
For the usage instructions head over to the [flite repo](https://github.com/festvox/flite) and refer the USAGE section
