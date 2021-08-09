import pysrt
from cv2 import cv2
import cliptest
import os
#import re

srt = pysrt.open("input.srt")
video="movie.mp4"

def writerpy(msg):
    file = open("script.rpy","a",encoding="utf-8")
    file.write(str(msg))
    file.write("\n")
    file.close()

def chack_rpy():
    if os.path.exists("script.rpy"):
        os.remove("script.rpy")


def get_video_duration(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num =cap.get(7)
        duration = frame_num/rate
        return duration
    return -1

def getallfps(v):
    cap=cv2.VideoCapture(video)
    return cap.get(7)

def get_f_t(label_t):
    timestr=str(label_t)
    timel1=timestr.split(",")
    timel2=timel1[0]
    timel2=timel2.split(":")
    timems=int(timel1[1])/1000
    time=timems+int(timel2[2])+int(timel2[1])*60+int(timel2[0])*60*60
    return time

def get_fps(st,nt,alltime,allfps):
    start=get_f_t(st)
    end=get_f_t(nt)
    belance=(start+end)/2
    per=belance/alltime
    fps=per*allfps
    return int(fps)

def use(t,n):
    a=t.split(n)
    return "".join(a)

def cn(text):
    #a=use(text, "'")
    b=use(text, '"')
    b=use(b, "\n")
    return b

if __name__=="__main__":
    chack_rpy()
    #prepare start
    writerpy("label start:")
    writerpy(" "*4+"play music bgm")
    #end
    ftp=0
    L=[]
    vl=get_video_duration(video)
    vf=getallfps(video)
    for i in range(len(srt)):
        content = srt.data[i]
        #print(content.text_without_tags)
        texts=content.text_without_tags
        if texts.find("{")==-1:
            ftp+=1
            si=get_fps(content.start,content.end,vl,vf)
            #print(si)
            L.append(si)
            writerpy(" "*4+"show b"+str(ftp)+" with fade")
            writerpy(" "*4+'"'+cn(texts)+'"')
            if ftp!=1:
                writerpy(" "*4+"hide b"+str(ftp-1))
    print(L)
    cliptest.getpic(L,video)
    #for i in range(len(L)):
    writerpy(" "*4+"return")

