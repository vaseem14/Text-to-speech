from gtts import gTTS
import os
import cv2

text = raw_input("Enter the text")
tts = gTTS(text=text, lang='en')
tts.save("test.mp3")
os.system("mpg321 test.mp3")
