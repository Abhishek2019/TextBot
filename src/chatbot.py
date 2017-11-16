import os
import random
import webbrowser


def file2list(filename):

    flist = []
    fr = open(filename)
    for line in fr.readlines():
        flist.append(line.strip())
    return flist


def write2file(filename,str):

    fr=open(filename,'a')
    str=str+"\n"
    fr.write(str)


def filelistgen(str):
    fpath=[]
    fname=[]
    for root, dirs, files in os.walk('/home'):
        for filename in files:
            if os.path.splitext(filename)[1] == str :

                fpath.append(os.path.join(root, filename))
                fname.append(filename)
    return fpath,fname

def playmusic(fpath,str):


    print("playing....")
    webbrowser.open(fpath[int(str)-1])


def showsongslist(filetype):
    no=1
    fpath,fname=filelistgen(filetype)
    for mp3file in fname:
        print(str(no)+" "+mp3file)
        no+=1
    return fpath


def robospeak(str):

    os.system("espeak '" + str + "'")
    print(str)


def humaninput():

    print("you : ", end="")
    return (input().strip())


robo=random.choice(("Hello  How are you feeling today?","Hi How are you feeling today?","whats up?"))
robospeak(robo)


human= humaninput()


while 1:

    if(human in file2list("../dataset/h_greeting_reply.txt")):
        robo=random.choice(("Thats Great so what would you like me to do?","Pleasure to hear that  so what would you like me to do?"))
        robospeak(robo)
    elif(("nice" in human.strip().split() or "good" in human.strip().split() or "fine" in human.strip().split()) and ("not" not in human.strip().split() or "no" not in human.strip().split() ) ):
        write2file("../dataset/h_greeting_reply.txt",human)

        robo=random.choice(("Thats Great so what would you like me to do?","Pleasure to hear that  so what would you like me to do?"))
        robospeak(robo)

    elif(human in ["run again"]):
        robo=random.choice(("so what would you like me again to do ?","would you like me to to execute any task?"))
        robospeak(robo)
    else:
        robo= "Its ok do not get too depressed so what would you like me to do?"
        robospeak(robo)


    human = humaninput()


    if(human in file2list("../dataset/music.txt")):
        robo=random.choice(("Here comes list of songs :","Here comes list","choose your song"))
        robospeak(robo)

        fpath=showsongslist(".mp3")
        human=humaninput()
        playmusic(fpath,human)


    elif(("show" in human.strip().split() or "play" in human.strip().split()) and ("songs" in human.strip().split() or "song" in human.strip().split() or "mp3" in human.strip().split())):
        write2file("../dataset/music.txt",human)

        robo = random.choice(("Here comes list of songs :", "Here comes list", "choose your song"))
        robospeak(robo)

        fpath=showsongslist(".mp3")
        human=humaninput()
        playmusic(fpath,human)

    elif():
        pass

    elif(human in ["stop","bye","no"]):
        robo = random.choice(("Thank you","I will take your leave","Bye sir","It was nice meeting you"))
        robospeak(robo)
        break

    human="run again"




















