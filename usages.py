from functions import *
from dicts import *

def read(item):
    if item == "letter":
        Output = "You read the content of the letter..\n\n\nThis is a very important message"
    elif item == "worksheet":
        Output = """
You read the content of the worksheet..\n\n
Aufgabenblatt: Mathematik

a) Berechne folgende aufgaben
1. Berechne x, wenn x + 3 = 4".
2. Berechne x, wenn 5x - 3 = 23.
3. Berechne y, wenn 2y + 3 = 11.
4. Berechne y, wenn 5x - 2 = 13.

b) Addiere all die vorherigen Lösungen und multipliziere sie mal 94,1

"""
    elif item == "classbook":
        Output = """
You read the content of the classbook..\n\n
Unterricht: Deutsch
Datum: 12.01.2010

Anwesenheitsliste

Name          Anwesenheit
---------------------------
Anna          Anwesend
Berta         Anwesend
Charlotte     Abwesend
Dieter        Anwesend
Erika         Anwesend
Frank         Abwesend
Greta         Abwesend
Hans          Anwesend
Ida           Anwesend
"""
    return Output

def cut(item):
    if item == "knife":
        Output = "You cut with knife"
        return Output

def spray(item, currentRoom):
    if item == "graffitican":
        TextToSpray = input("What do you want to spray against the walls?\n")
        rooms[currentRoom]["message"] += "\nThere is a graffiti with the label " + TextToSpray + " on the walls."
        Output = f"You sprayed {TextToSpray} against the walls"
        return Output

def TakeAction(IntendetUse, item, currentRoom):
    if IntendetUse == "read":
        Output = read(item)
    elif IntendetUse == "cut":
        Output = cut(item)
    elif IntendetUse == "start":
        Output = startDevice(item)
    elif IntendetUse == "spray":
        Output = spray(item, currentRoom)
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
