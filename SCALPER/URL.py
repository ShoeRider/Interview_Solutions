#pip3 install pytube
#Common issues: https://github.com/nficano/pytube/issues/381
from pytube import YouTube

#sudo pip install requests
import requests
import time

#pip install BeautifulSoup4
from bs4 import BeautifulSoup


import subprocess
import os
import re
import sys
#pip install moviepy
from moviepy.editor import VideoFileClip
#sudo pip install colorama
from colorama import Fore, Back, Style

import json

def Request(URL):
    return {}


from bs4 import BeautifulSoup
class Text():
    def __init__(self,*args,**kwargs):
        self.String = str(String)
        print(kwargs,("nGrams" in kwargs))

        if("nGrams" in kwargs):
            self.nGrams = kwargs["nGrams"]
            self.nGramSequence = self.Find_nGrams(self.String,self.nGrams)
        if("HTML" in kwargs):
            self.BS = BeautifulSoup(self.String, "html.parser")
        #self.

    def _BS_Find(self):
        JS_Discription = self.BS.find('yt-formatted-string',attrs={'class':'content style-scope ytd-video-secondary-info-renderer'})
    def RemoveCharacters(self,Characters):

        NewString = self.String
        for remove in Characters:
            NewString = NewString.replace(remove, '')
        return NewString
    def Find_nGrams(self,String,nGrams):
        StringList   = String.split(" ")
        nGramSequence = {}

        for OffSet in range(0,len(StringList)-(nGrams),1):
            String = ""
            for Word in StringList[OffSet:OffSet + nGrams]:
                String += Word + " "
            SubSequence = String[:len(String)-1]
            if (SubSequence not in nGramSequence):
                nGramSequence[SubSequence] = []

            nGramSequence[SubSequence].append(OffSet)
        return nGramSequence
    def Find_UniqueAndOverlapping_Elements(self,PassThrough):
        if(type(PassThrough)==type(type(str()))):
            Temp = _String(PassThrough,nGrams=self.nGrams)
        else:
            Temp = PassThrough

        OverLappingElements = 0
        UniqueElements = len(self.nGramSequence)

        for element_1 in self.nGramSequence:
            if element_1 in Temp.nGramSequence:
                OverLappingElements += 1
            else:
                UniqueElements += 1

        return (OverLappingElements,UniqueElements)
    #Find_JaccardSimilarityCoefficient
    def Find_JSC(self,PassThrough):
        (OverLappingElements,UniqueElements) = self.Find_UniqueAndOverlapping_Elements(PassThrough)
        JaccardIndex = OverLappingElements/UniqueElements
        return JaccardIndex
    def Find_JD(self,PassThrough):
        (OverLappingElements,UniqueElements) = self.Find_UniqueAndOverlapping_Elements(PassThrough)

        JaccardDistance = (UniqueElements-OverLappingElements)/UniqueElements
        return JaccardDistance

#<a class=ABC>
#('a','class','ABC')


class _SCALPER():
    def __init__(self,URL:str):
        self.URL_Location   = URL
        self.HTML           = requests.get(self.URL_Location)
        self.BS             = BeautifulSoup(self.HTML.text, "html.parser")
        #print(self.BS)
    def _BS_Find(self):
        #,attrs={'class':'yt-uix-tile-link'})
        for X in self.BS.findAll('div'):
            print(X)

        href_List = self.BS.findAll('href')
        print(href_List)
        print(self.BS.find("h1"))#,attrs={'class':"style-scope ytd-video-primary-info-renderer"}
        print(self.BS.find('yt-formatted-string',attrs={'class':'content style-scope ytd-video-secondary-info-renderer'}))
    def Ignore(self):
        #print(self.BS.find("yt-formatted-string",attrs={PageRoutine[1]:PageRoutine[2]}))
        d = {}
        PageRoutines =[('yt-formatted-string','class','style-scope ytd-video-primary-info-renderer','YOUTUBE_Title')]
        for PageRoutine in PageRoutines:
            print(PageRoutine[0],",",PageRoutine[1],",",PageRoutine[2],",",PageRoutine[3])
            d[PageRoutine[3]] = self.BS.find(PageRoutine[0],attrs={PageRoutine[1]:PageRoutine[2]})
        print(d)

if True:
    Test = _SCALPER("https://www.youtube.com/watch?v=CO4ifMknS84")
    Test._BS_Find()

if False:
    TestHTML = """<yt-formatted-string force-default-style="" class="style-scope ytd-video-primary-info-renderer">CUDA In Your Python: Effective Parallel Programming on the GPU</yt-formatted-string> """
    BS             = BeautifulSoup(TestHTML, "html.parser")
    print(BS.find("yt-formatted-string",attrs={'class':"style-scope ytd-video-primary-info-renderer"}))

class _URL(object):
    def __init__(self):
        self.URL = URL

class URL(_URL):
    def __init__(self,*args, **kwargs):
        self.URL = _String(*args, **kwargs)
        self.pattern = re.compile("^(?:https://|http://)")
        self.Regex = ["(?:https://|http://)"]
        self.RegexString = self.GetRegex()
        self.Links = {}
        self.Data = {}
        self.SCALPER = _SCALPER(self.URL)
        LinuxCharacterSanitizer = ":?|;,.$@%#^*`\"\\/'"

def URL_List(self):
    def __init__(self,Length):
        self.Integer = Integer







if(False):
    string_0 = "Walkin the dog at the park"
    temp_0 = _String(string_0,nGrams=2)
    string_1  = "Walkin  dog at the park"
    temp_1 = _String(string_1,nGrams=2)
    print(temp_0)
    print(temp_0.nGramSequence)
    print(temp_0.Find_JSC(temp_1))
    print(temp_0.Find_JD(temp_1))


import urllib.request
import os
import re
import sys

if False:
    print("Including PyQt5")
    from PyQt5.QtWebEngineWidgets import QWebEnginePage
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    Dir = ""
    class Page(QWebEnginePage):
        def __init__(self, url):
            self.app = QApplication(sys.argv)
            QWebEnginePage.__init__(self)
            self.html = ''
            self.loadFinished.connect(self._on_load_finished)
            self.load(QUrl(url))
            self.app.exec_()
        def _on_load_finished(self):
            self.html = self.toHtml(self.Callable)
            print('Load finished')
        def Callable(self, html_str):
            self.html = html_str
            self.app.quit()






class _URL_YT_Video(_URL):
    def __init__(self,*args, **kwargs):
        self.URL = str(*args, **kwargs)
        self.Regex:["(?:https://|http://)"]
class YT_Page():
    def __init__(self,URL):
        self.Page = Page(URL)
        self.soup = bs.BeautifulSoup(self.Page.html, 'html.parser')

        self.Dic = {}
        self.Dic["Discription"] = self.GetYT_Discription()
        self.Dic["LikeDislike"] = self.GetYT_LikeDisLike()
    def GetYT_Discription(self):
        JS_Discription = self.soup.find('yt-formatted-string',attrs={'class':'content style-scope ytd-video-secondary-info-renderer'})
        return (JS_Discription.text)
    def GetYT_LikeDisLike(self):
        print()
        #yt-formatted-string
    def GetDict(self):
        return self.Dic

class _URL_Site(_URL):
    def __init__(self,URL,regex):
        self.URL = _URL(URL)
        self.Regex:["(?:https://|http://)"]

class URL_Manager():
    def __init__(self):
        self.Site = {}

        self.URL  = str(*args, **kwargs)
    def Add_Site(self,url):
        return 0


class ALL_URLs():
    def __init__(self):
        self.URL_ClassList={
        "YT_Video":_URL_YT_Video,
        "YT_Channel":_URL_YT_Channel,
        }
        self.All_URLTypes = {}
        for URLType in self.URL_ClassList.keys():
            self.All_URLTypes[URLType] = self.URL_ClassList[URLType]()
        self.ALL_URLs = {}
    def Get_URL(self):
        return ""

def Test3():
    YTURL = YT_URLManager("https://stackoverflow.com/questions/15483230/in-python-can-you-do-prototyping-of-string-functions-like-in-javascript")
    print(YTURL)
    print(YTURL.YT_Hash)
