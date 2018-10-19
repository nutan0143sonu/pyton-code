from gtts import gTTS
import os
tts=gTTS(text='hello sonu siwach how are you and where are you working now days',lang='en')
tts.save('nutan.mp3')
os.system('mpg321 sonu.mp3')
