import pyttsx3
import wikiquotes
import random 
import re


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#text cleaning function to eliminate parenthesis and backslash.
def text_clean(text):
    text = re.sub("\\\\",'',text)
    text = re.sub(r'\([^)]*\)', '', text)
    return text

#you can always add more speakers
speakers = ["inspiration","tonny robbins", "love","life","les brown",
            "eric thomas","jim rohn","brian tracy","mel robbins"]

def tell_quote(how_many =1):    
    quotes = wikiquotes.get_quotes(random.sample(speakers,how_many),"english")
    acceptables = []
    
    for quote in quotes:
        length = len(quote.split(" "))
        sents = len(quote.split("."))
        if length>5 and sents<=10:
            acceptables.append(quote)
    
    tell_quote = random.sample(acceptables,1)
    tell_quote = text_clean(tell_quote)
    
    speak(tell_quote)