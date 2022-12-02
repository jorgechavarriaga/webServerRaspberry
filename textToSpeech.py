from gtts import gTTS
import os

#mytext = 'Welcome to ChavaZystem Tech!'
#language = 'en'

def textToSpeech(msg,language):
        try:
                #mytext = 'Welcome to ChavaZystem Tech!'
                #language = 'en'
                myobj = gTTS(text=msg, lang=language, slow=False)
                myobj.save("welcome.mp3")
                #os.system("mpg321 welcome.mp3")
                print('Ok')
                return os.system("mpg321 welcome.mp3")
        except Exception as ex:
                print('Something went wrong!')
