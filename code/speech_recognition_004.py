from gtts import gTTS
import os
tts=gTTS(text='I am fine and i am working in Maruti company now days',lang='en')
tts.save('nutan.wav')
os.system('mpg321 sonu1.wav')
