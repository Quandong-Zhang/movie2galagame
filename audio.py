import os

def chack_file(name):
    #name=str(name)
    if os.path.exists(name):
        os.remove(name)

def get_audio(fname):
    chack_file("audio.mp3")
    cmd="ffmpeg.exe -i "+str(fname)+" -vn audio.mp3"
    os.system(cmd)

def cut_audio(name,s,e):
    print(s)
    print(e)
    nd=e-s
    chack_file("./audio/a"+str(name)+".mp3")
    cmd="ffmpeg.exe -i audio.mp3 -ss "+str(s)+" -t "+str(nd)+" ./audio/a"+str(name)+".mp3"
    print(cmd)
    os.system(cmd)

if __name__=="__main__":
    #get_audio("movie.mp4")
    cut_audio(1, 71.39, 75.52)
