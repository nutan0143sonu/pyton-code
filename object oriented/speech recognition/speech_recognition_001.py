#import speech recognizer
import speech_recognition as sr
mic_name=" "# its used for store device name
sample_rate=48000#sample rate is how often values are recorded.kitni jldi vo google ko bhejega
chunk_size=4096# 2048 it is buffer that fix how many words it pass in chunk.kitna record krega one time

r=sr.Recognizer()
#generate a list of all audio card/microphone
mic_list=sr.Microphone.list_microphone_names()
print(mic_list)
print('-'*20)
print(list(enumerate(mic_list)))
print('-'*20)
device_id=1
with sr.Microphone(device_index=device_id,sample_rate=sample_rate,chunk_size=chunk_size)as source:
    r.adjust_for_ambient_noise(source)
    print("say somthing")
    #listens for user's input
    audio=r.listen(source)
    print("1")
    try:
        text=r.recognize_google(audio)
        #r.recognize_google(audio,key="GOOGle_Speech-RECOGNITION_API_KEY")
        print("you said: "+ text)
    except sr.UnknownValueError:
        print("Google speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("could not request result from Googlr\
                 speech Recognition service; {0}".format(e))
