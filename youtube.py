from urllib.request import urlopen
import urllib.parse
import webbrowser
from sys import platform
import os

def youtube(textToSearch):
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open_new_tab(url)


if __name__ == '__main__':
    youtube('any text')
