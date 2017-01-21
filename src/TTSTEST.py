import talkey
from gtts import gTTS
from pygame import mixer
import subprocess

tts = gTTS(text='This is a Test. Do not panic.', lang='en')
print("STart")
tts.save("speech.mp3")
print("End")

subprocess.Popen(['mpg123', '-q', "speech.mp3"]).wait()