from functions import *
from dicts import *

def read(item):
    if item == "letter":
        Output = "You read the content of the letter..\n\n\nThis is a very important message"
        return Output

def cut(item):
    if item == "knife":
        Output = "You cut with knife"
        return Output

def TakeAction(IntendetUse, item):
    if IntendetUse == "read":
        Output = read(item)
    elif IntendetUse == "cut":
        Output = cut(item)
    elif IntendetUse == "start":
        Output = startDevice(item)
    return Output

def startDevice(device):
    Output = ""
    if device == "laptop":
        loopControl = True
        while loopControl:
            move = ''
            while move == '': 
                print('''
    Welcome to your laptop
    Commands:
        read [file]
        copy [usbdrive]
        start [program]
    ''')        
                print("\n----------------------------------------------\n")
                print("files:\n")
                fileList = list(filesOnLaptop.keys())
                for item in fileList:
                    print(item)
                print("\n" + Output)
                move = input('>')
                move = move.lower().split()
                
                if move[0] == "read":
                    if len(move) < 2:
                        Output = "You have to specify a file to read"
                    else:
                        file = move[1]
                        if file in fileList:
                            if "content" in filesOnLaptop[file]:
                                Output = f"You are reading the file {file}\n" + filesOnLaptop[file]["content"]
                            else:
                                Output = f"{file} doesnt have any content"
                        else:
                            Output = f"{file} doesnt exist!"
                if move[0] == "start":
                    if len(move) < 2:
                        Output= "You have to specify a program to start"
                    else:
                        program = move[1]
                        if program in fileList:
                            isProgram = filesOnLaptop[program]["isProgram"]
                            if isProgram != 0:
                                if program == "trojan":
                                    infected = filesOnLaptop["trojan"]["connected"]
                                    if infected == 0:
                                        Output = f"The Trojan has no connections from infected mashines yet\nActive computers: {infected}"
                                    else:
                                        Output = f"The Trojan has {infected} active infected computers"
                            else:
                                Output = f"The {program} that you are trying to run is not a program"
                        else:
                            Output = f"{file} doesnt exist!"
                if move[0] == "exit":
                    typingEffect("Shutdown of laptop initiated...", 0.05)
                    loopControl = False


    return Output
