import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    speech = r.recognize_google(audio)
    print("You said: " + speech)
    tts = gTTS(text = speech, lang = 'en')
    tts.save("repeat.mp3")
    playsound("repeat.mp3")
    #os.system("start repeat.wav")
    #os.system("TASKKILL /F /IM wmplayer.exe")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
