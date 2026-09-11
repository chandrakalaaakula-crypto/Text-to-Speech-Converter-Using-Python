import os
from gtts import gTTS
text=("hi this chandrakala how are u")
tts=gTTS(text=text,lang='en')
tts.save("test.mp3")
print("Audio saved")
os.system("start test.mp3")
