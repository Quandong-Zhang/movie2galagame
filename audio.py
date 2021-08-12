import os

def chack_file(name):
    name=str(name)
    if os.path.exists(name):
        os.remove(name)

def get_audio(fname):
    chack_file("audio.mp3")
    cmd="ffmpeg.exe -i "+str(fname)+" -vn audio.mp3"
    os.system(cmd)

def cut_audio(name,s,e):
    chack_file("./audio/"+str(name)+".mp3")
    cmd="ffmpeg.exe -i audio.mp3 -ss "+str(s)+" -t "+str(e)+" ./audio/"+str(name)+".mp3"
    os.system(cmd)

if __name__=="__main__":
    #get_audio("movie.mp4")
    cut_audio(1, 200, 300)
