#python 3.x program to tanscribe an audio file
import speech_recognition as sr
Audio_File=("C:\Python\Python36-32\speech recognition project/nutan1.mp3")
#use the audio file as the audio source
r=sr.Recognizer()
with sr.AudioFile(Audio_File) as source:
    #read the audio file.here we use record instead of
    #listen
    audio=r.record(source)
try:
    print("The audio file contains:" +r.recognize_goggle(audio))
except sr.UnknownValueError:
    print("Google speech Recognition could not understand audio")
except sr.RequestError as e:
    print("could not request result from Google\
                 speech Recognition service; {0}".format(e))
