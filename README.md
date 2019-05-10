# English to Telugu Video Translator
### About this project
Initial version was developed as part of UC Berkeley Open Innovation Hackathon, India - 2017 (Winner project in Communications vertical) and later underwent various improvements as a part of major project during our undergrad. This application mainly focuses on translation of English videos into Telugu. 

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
