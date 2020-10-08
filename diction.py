#from difflib import get_close_matches
import pyttsx3
#import json
import re
import speech_recognition as sr
from io import StringIO 
import sys
from PyDictionary import PyDictionary
from spellchecker import SpellChecker

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        
#data = json.load(open('data.json'))
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
dictionary = PyDictionary()
spell = SpellChecker()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query

def tell_meaning(word):
    with Capturing() as output:
        value = dictionary.meaning(word)    
    if len(output) != 0: 
        error_message = output[0]
        if "list index out of range" in error_message:
            return "get_correction"
        elif "HTTPConnectionPool" in error_message:
            return "network_problem"
        else:
            return "too many words"
    else:
        keys = value.keys()
        string_to_tell = ''
        for key in keys:
            string_to_tell += "As a " + key + " meaning is " + ','.join(value[key]) + '. '
        string_to_tell = re.sub("\(",'',string_to_tell)
        
        print(string_to_tell)
        return value

def translate(word):
    word = word.lower()
    value = tell_meaning(word)
    if value not in ['get_correction','network_problem','too many words']:
        speak(value)
    elif value == 'network_problem':
        speak('your network is off. please turn it on.')
    elif value == 'too many words':
        speak("please tell one word at a time.")
    elif value == "get_correction":
        word_corr = spell.correction(word)
        speak('Did you mean ' + word_corr +
              ' instead,  respond with Yes or No.')
        print("word_corrected:", word_corr)
        ans = takeCommand().lower()
        if 'yes' in ans:
            speak(tell_meaning(word_corr))
        elif 'no' in ans:
            speak("Word doesn't exist. Please make sure you spelled it correctly.")
        else:
            speak("We didn't understand your entry.")
    else:
        speak("Word doesn't exist. Please double check it.")

    
#def translate(word):
#    word = word.lower()
#    if word in data:
#        speak(data[word])
#    elif len(get_close_matches(word, data.keys())) > 0:
#        x = get_close_matches(word, data.keys())[0]
#        speak('Did you mean ' + x +
#              ' instead,  respond with Yes or No.')
#        ans = takeCommand().lower()
#        if 'yes' in ans:
#            speak(data[x])
#        elif 'no' in ans:
#            speak("Word doesn't exist. Please make sure you spelled it correctly.")
#        else:
#            speak("We didn't understand your entry.")
#
#    else:
#        speak("Word doesn't exist. Please double check it.")


if __name__ == '__main__':
    translate("")
