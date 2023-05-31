
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wakeword = "hi computer"
stop_it = False
usevoice = True

def dotalk(text):
    print(text)

    if (usevoice==True):
        engine.say(text)
        engine.runAndWait()


def callback(recognizer, audio):                          # this is called from the background thread
    try:
        command = None
        global stop_it
        global usevoice
        if (audio is not None):
            try:
                command = recognizer.recognize_google(audio)
                print(command)
            except:
                pass
            
            if (command is not None):

                if (wakeword in command):
                    command = command.replace(wakeword, '').strip()
                
                    if ('voice off' in command):
                        usevoice=False
                        dotalk("Voice Off")
                    elif ('voice on' in command):
                        usevoice=True
                        dotalk("Voice On")

                    elif ('terminate' in command):
                        stop_it=True
                        dotalk("End Program")

                    elif 'time' in command:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        dotalk('Current time is ' + time)

                    elif 'date' in command:
                        dotalk('sorry, I have a headache')

                    elif 'are you single' in command:
                        dotalk('I am in a relationship with my dogs')

                    elif 'joke' in command:
                        dotalk(pyjokes.get_joke())
                    
                    elif 'play' in command:
                        song = command.replace('play', '').strip()
                        dotalk('playing ' + song)
                        pywhatkit.playonyt(song)
                  
                    elif 'who is' in command:
                        person = command.replace('who is', '').strip()
                        try:
                            info = wikipedia.summary(person, 1)
                        except:
                            info = "I cannot find that a page for " + person

                        dotalk(info)

                    elif 'what is' in command:
                        item = command.replace('what is', '').strip()
                        try:
                            info = wikipedia.summary(item, 1) 
                        except:
                            info = "I cannot find that a page for " + item
                        dotalk(info)
                        
                  

                    else:#print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
                        dotalk('please say the command again')
                    


        
    except LookupError:
        dotalk("Parlez vous anglais?")




    
r = sr.Recognizer()

m = sr.Microphone()
#r.energy_threshold = 836.8677848144149
r.dynamic_energy_threshold=True
r.pause_threshold=1




print("Listening...")
with m as source: 
    r.adjust_for_ambient_noise(source)      # we only need to calibrate once, before we start listening
#stop_listening = r.listen_in_background(m, callback,phrase_time_limit=5)
stop_listening = r.listen_in_background(m, callback)


while True:
    if stop_it:
        stop_listening(wait_for_stop=True)
        break
    time.sleep(0.1)                                  # call the stop function to stop the background thread
