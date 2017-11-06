import os
import random
import webbrowser
from pygame import mixer
import speech2text as s2t


for i in range(1):

    robo=random.choice(("Hello  How are you feeling today?","Hi How are you feeling today?","whats up?"))
    os.system("espeak '"+robo+"'")

    print(robo)

    print("you : ",end="")
    human=input().strip()

    while 1:
        if(human in ["I am fine","Thank you","nice day"]):
            robo=random.choice(("Thats Great so what would you like me to do?","Pleasure to hear that  so what would you like me to do?"))
            os.system("espeak '"+robo+"'")
            print(robo)
        elif(human in ["run again"]):
            robo=random.choice(("so what would you like me to do?"))
            os.system("espeak '"+robo+"'")
            print(robo)

        print("you : ", end="")
        human = input().strip()



        if(human in ["play mp3","play something","play song"]):
            robo=random.choice(("Here comes list of songs :","Here comes list","choose your song"))
            os.system("espeak '"+robo+"'")
            print(robo)


            def mp3gen():
                for root, dirs, files in os.walk('/home'):
                    for filename in files:
                        if os.path.splitext(filename)[1] == ".mp3":
                            yield os.path.join(root, filename)


            for mp3file in mp3gen():
                print(mp3file)
            print("you : ",end="")
            human=input().strip()
            print("playing....")

            webbrowser.open(human)
        elif(human in ["stop","bye"]):
            break
        human="run again"
        continue

















