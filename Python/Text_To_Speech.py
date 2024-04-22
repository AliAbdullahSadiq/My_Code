from gtts import gTTS
import os

def text_to_speech(text, language='en',  filename='/Users/ayesha/Desktop/tts/output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    

if __name__ == """ Hello Saad bhai
"""

    text_to_speech(text)
