#coding:utf-8
'''
Created on 2015/02/26

@author: kubodera
'''
import subprocess
import config
from datetime import datetime
import cv2
import time
img1 = cv2.imread('apa_close_small.png')
img2 = cv2.imread('apa_open_small.png')
imgA = cv2.imread('apa_A.png')
imgI = cv2.imread('apa_I.png')
imgU = cv2.imread('apa_U.png')
imgE = cv2.imread('apa_E.png')
imgO = cv2.imread('apa_O.png')
import threading
apa_alarm = False
c = True
sentenceList = []

class SpeechWithAI():
    
    def __init__(self):
        
        print "check"
        #url = 'http://localhost:8080/loginNoSns/6d1bda61-941f-4f86-aa19-29aac7fb75ad'
        #req = urllib2.Request(url)
        #req.add_header('Content-Type', 'application/json')
        #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36')
        #response = urllib2.urlopen(req).read()
        #res = json.loads(response.decode('utf-8'))
                                    
    def apaSpeak(self, line): 
        if config.apaspeak == 0:              
            if 'さようなら' in line:
                subprocess.call('say -vKyoko -r200 "当ホテルを利用していただき、ありがとうございました。お気をつけておかえりくださいませ。"', shell=True)
                config.c = False
            elif '時間' in line:
                #c = threading.activeCount()
                print config.c    
                time = datetime.now()
                hour = time.strftime('%H')
                minutes = time.strftime('%M')
                subprocess.call('say -vKyoko -r200 "ただいまの時刻は"' + hour + '時' + minutes + '分です。', shell=True)
                config.c = False
                print config.c
            elif '誰' in line:
                subprocess.call('say -vKyoko -r200 "私はアパ社長人工知能です。"', shell=True)
                config.c = False
            elif 'チェックイン' in line:
                subprocess.call('say -vKyoko -r200 "ただいま深夜のため、受付がおりません。受付の係りの者を呼びますので、少々お待ちください。"', shell=True)
                config.c = False
            elif 'おはよう' in line:
                subprocess.call('say -vKyoko -r200 "おはようございます。今回のご宿泊はいかがでしたでしょうか。"', shell=True)
                config.c = False
                config.apaspeak = 1
            else:
                subprocess.call('say -vKyoko -r200 "私はアパ社長人工知能です。"', shell=True)
                config.c = False
        elif config.apaspeak == 1:
            if 'よかった' in line or '良かった' in line:
                subprocess.call('say -vKyoko -r200 "それはよかったです。またのご利用をお待ちしております。"', shell=True)
                config.c = False
                config.apaspeak = 0
            elif 'まあまあ'  in line or '普通' in line:
                subprocess.call('say -vKyoko -r200 "ありがとうございます。ご要望などありましたら、承ります。"', shell=True)
                config.c = False
                config.apaspeak = 2
            elif '悪い'  in line or '最悪' in line:
                subprocess.call('say -vKyoko -r200 "大変申し訳ございませんでした。ご要望等ございましたら、承ります。"', shell=True)
                config.c = False
                config.apaspeak = 2
            else:
                subprocess.call('say -vKyoko -r200 "もう一度おっしゃってください。"', shell=True)
                config.c = False
        elif config.apaspeak == 2:
            if line != '':
                subprocess.call('say -vKyoko -r200 "承りました。今後とも当ホテルをよろしくお願いいたします。"', shell=True)
                config.c = False
                config.apaspeak = 0
    
    def apaSpeakEnglish(self, line):
        global sentenceList
        sentence = "" 
        if config.apaspeak == 0:              
            if 'check in' in line:
                sentence = "For the middle of the night, a receptionist is not now. I will call the person in charge of the reception desk, wait a minute." 
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence , shell=True)
                config.c = False 
            elif 'good morning' in line:
                sentence = "Good morning, how can I help you?"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False        
            elif 'hello' in line:
                sentence = "Hello, how can I help you?"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False
            elif 'good night' in line:
                sentence = "Good night"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False    
            elif 'room' in line:
                sentence = "Yes, we have some rooms available"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False
            elif 'air-conditioning' in line:
                sentence = "Yes,all the room have air-conditioning"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False
            elif 'reservation' in line:
                sentence = "Let me look on the system. Yes, Akshay a single room for 2 nights, bed and breakfast?"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False	
            elif 'breakfast' in line:
                sentence = "Morning at 9am"
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False
            else:
                sentence = "please say one more time" 
                subprocess.call('say -v' + config.speaker + ' -r' + config.speed + sentence, shell=True)
                config.c = False
        sentenceList = list(sentence)
        outputlist = self.makeAIUEO(sentenceList)
        return outputlist
                
    def makeAIUEO(self, arg):
        listlen = len(arg)
        i = 0
        while i < listlen:
            if "a" != arg[i] and "i" != arg[i] and "u" != arg[i] and "e" != arg[i] and "o" != arg[i] and " " != arg[i]:
                del arg[i]
                listlen -= 1
            else:
                i += 1
        return arg
        
    def apaImageEnglish(self, line):      
        global img1, img2, imgO, imgU, imgA, imgE, imgI, sentenceList
        connectimg = {"o":0, "u":1, "a":2, "e":3, "i":4, " ":5}
        imglist = [imgO, imgU, imgA, imgE, imgI, img1]
        wordtime = 50
        config.c = True
        if config.apaEnglish:
            w = threading.Thread(target=self.apaSpeakEnglish, args = (line,))
        else:
            w = threading.Thread(target=self.apaSpeak, args = (line,))
        w.start()
        while config.c:
            for i in sentenceList:
                print i
                cv2.imshow('result', imglist[connectimg[i]])
                cv2.waitKey(wordtime)
                """
                if voice_U:
                    cv2.imshow('result', imgU)
                    cv2.waitKey(wordtime)
                elif voice_A:
                    cv2.imshow('result', imgA)
                    cv2.waitKey(wordtime)
                elif voice_E:
                    cv2.imshow('result', imgE)
                    cv2.waitKey(wordtime)
                elif voice_I:
                    cv2.imshow('result', imgI)
                    cv2.waitKey(wordtime)
                elif voice_O:
                    cv2.imshow('result', imgO)
                    cv2.waitKey(wordtime)
                else:
                    cv2.imshow('result', img2)
                    cv2.waitKey(spacetime)
                """
            #cv2.imshow('result', img2)
            #cv2.waitKey(200)
            #cv2.imshow('result', img1)
            #cv2.waitKey(200)
            
            
if __name__=='__main__':
    #spe = SpeechWithAI()
    #spe.apaImage('check in')
    spe = SpeechWithAI()
    list = list("nfduisphaf jdas")
    print list
    print spe.makeAIUEO(list)
    
    #connectimg = {"o":1, "u":2, "a":3, "e":4, "i":5}
    #imglist = [imgO, imgU, imgA, imgE, imgI]
    #print connectimg["e"]
    #print imglist[4]
    #cv2.imshow('result', imglist[connectimg["e"]])
    subprocess.call('say -v Ralph -r' + config.speed + "Please say one more time", shell=True)
    
    
    
            

    
    
    
    
    
