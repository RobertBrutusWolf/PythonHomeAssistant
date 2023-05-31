#sudo apt install portaudio19-dev python3-pyaudio
#conda install PyAudio
import os 
import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence


# initialize the recognizer
r = sr.Recognizer()


with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=8)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)