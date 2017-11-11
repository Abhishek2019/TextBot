import os
import random
import webbrowser


def file2list(filename):

    flist=[]
    fr = open(filename)
    for line in fr.readlines():
        flist.append(line.strip())
    return flist


def write2file(filename,str):

    fr=open(filename,'a')
    str=str+"\n"
    fr.write(str)


def mp3gen():

    for root, dirs, files in os.walk('/home'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

def playmusic(str):

    print("playing....")
    webbrowser.open(str)


def showsongslist():

    for mp3file in mp3gen():
        print(mp3file)


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
    elif("nice" in human.strip().split() or "good" in human.strip().split() or "fine" in human.strip().split()):
        write2file("../dataset/h_greeting_reply.txt",human)

        robo=random.choice(("Thats Great so what would you like me to do?","Pleasure to hear that  so what would you like me to do?"))
        robospeak(robo)

    elif(human in ["run again"]):
        robo=random.choice(("so what would you like me again to do?","would you like me to to execute another task?"))
        robospeak(robo)
    else:
        robo=random.choice(("It's ok don't get depressed  so whatwould you like me to do?"))
        robospeak(robo)


    human = humaninput()


    if(human in file2list("../dataset/music.txt")):
        robo=random.choice(("Here comes list of songs :","Here comes list","choose your song"))
        robospeak(robo)

        showsongslist()
        human=humaninput()
        playmusic(human)


    elif("play" in human.strip().split() and ("song" in human.strip().split() or "mp3" in human.strip().split())):
        write2file("../dataset/music.txt",human)

        robo = random.choice(("Here comes list of songs :", "Here comes list", "choose your song"))
        robospeak(robo)

        showsongslist()
        human=humaninput()
        playmusic(human)


    elif(human in ["stop","bye","no"]):
        robo = random.choice(("Thank you","I will take your leave","Bye sir","It was nice meeting you"))
        robospeak(robo)
        break

    human="run again"




















