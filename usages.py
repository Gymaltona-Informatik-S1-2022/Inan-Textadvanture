from functions import *
from dicts import *
import time
import sys
from datetime import datetime, timedelta

starttime = 0

def timer_start():
    global starttime
    starttime = time.time()

def read(item):
    if item == "letter":
        Output = """
You read the content of the letter..\n\n\n

Sehr geehrte Frau Müller,

ich schreibe Ihnen heute wegen unseres Schülers Jacob Gutsmann, der in Ihrer Klasse in der 10. Klasse ist.
Leider habe ich in letzter Zeit einige Beschwerden von anderen Lehrern und Schülern über Jacobs Verhalten und Leistungen erhalten.

Seine Noten sind in den letzten Monaten stark abgefallen und er scheint sich wenig für den Unterricht zu interessieren.
Auch gibt es Berichte über undiszipliniertes Verhalten und mangelnden Respekt gegenüber anderen Schülern und Lehrern.

Ich bin mir sicher, dass Jacob das Potential hat, sich zu verbessern, aber ich fürchte,
dass er ohne gezielte Unterstützung und Förderung Schwierigkeiten haben wird, sein Potential auszuschöpfen.
Deshalb würde ich gerne mit Ihnen zusammenarbeiten, um Jacob zu helfen, seine Leistungen zu verbessern und sich besser in der Klasse zu integrieren.

Ich hoffe, dass wir gemeinsam eine Lösung finden können, um Jacobs Fortschritte zu unterstützen.

Mit freundlichen Grüßen,
Frau Lindenau

"""
    elif item == "paper":
        Output = """
You read the content of the paper..\n\n

Sehr geehrter Frau Lindenau,

ich schreibe Ihnen heute im Zusammenhang mit dem Passwort für den Server-Datenbank-Administrator.
Das aktuelle Passwort wurde geändert und lautet nun "CoronaOutbreak2020".

Bitte beachten Sie, dass dieses Passwort vertraulich behandelt werden muss und nur von autorisierten Personen genutzt werden darf.
Sollten Sie das Passwort vergessen haben oder es mit jemandem teilen müssen,
wenden Sie sich bitte an mich oder das IT-Team, damit wir Ihnen in diesem Fall weiterhelfen können.

Ich hoffe, dass diese Information für Sie von Nutzen ist und stehe Ihnen gerne für weitere Fragen zur Verfügung.

Mit freundlichen Grüßen,
Herr Schroller
IT-Team des Gymnasium Altonas
"""
    elif item == "worksheet":
        Output = """
You read the content of the worksheet..\n\n
Aufgabenblatt: Mathematik

a) Berechne folgende aufgaben
1. Berechne x, wenn x + 5 = 8 ".
2. Berechne x, wenn 5x - 7 = 23.
3. Berechne y, wenn 2y + 3 = 19.
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
    elif item == "encyclopedia":
        Output = """
You read the content of the encyclopedia..\n\n

rösche sind kleine, vierbeinige, meist grüne Amphibien, die hauptsächlich in der Nähe von Wasser leben. Sie haben lange, kräftige Hinterbeine,
die ihnen ermöglichen zu springen und zu schwimmen. Frösche haben auch eine dicke, feuchte Haut, die ihnen hilft,
Feuchtigkeit zu speichern und ihre Körpertemperatur zu regulieren.

Frösche ernähren sich hauptsächlich von Insekten und anderen kleinen Tieren, die sie mit ihrer langen,
rundlichen Zunge fangen. Manche Frösche sind auch fähig, kleinere Frösche und sogar Mäuse zu fressen.

Es gibt viele verschiedene Arten von Fröschen auf der ganzen Welt, von den kleinen,
farbenfrohen Froschlurchen bis hin zu den großen, grünen Baumfröschen. Einige Frösche sind in der Lage,
laut zu quaken oder zu rufen, während andere eher leise sind.

Frösche spielen eine wichtige Rolle in vielen Ökosystemen als Bestäuber und als Nahrung für größere Tiere.
Sie sind auch ein wichtiger Indikator für die Umweltgesundheit, da sie empfindlich auf Veränderungen in ihrem Lebensraum reagieren.

In vielen Kulturen sind Frösche auch symbolisch und spielen in Märchen, Legenden und Mythen eine Rolle.
Sie werden oft als Glücksbringer betrachtet und finden sich in Kunst, Literatur und Musik wieder.

"""
    return Output

def GetTime(item, inventory):
    global starttime
    if item == "watch":
        if "watch" in inventory:
            GameClock = datetime(1900, 1, 1, 1, 0, 0)
            minutes = round((time.time() - starttime)/60)
            currentTime = GameClock + timedelta(minutes=round(minutes))
            Output = f"Current Time is: {currentTime.strftime('%I:%M')}"
        else:
            Output = "You dont have a watch to look up the time with"
    else:
        Output = f"You cant get the time with a {item}"
    return Output


def cut(item, currentRoom, inventory):
    global starttime
    if item == "boltcutters":
        sure = input("Are you sure you want to cut the lock of the bike and leave the scene?\nIt will end the game. [Y/N]\n")
        if sure == "Y":
            endgame(starttime, inventory)
            return Output
        else:
            Output = "You didn't cut the lock and you can continue playing"
            return Output

def spray(item, currentRoom):
    if item == "graffitican":
        TextToSpray = input("What do you want to spray against the walls?\n")
        rooms[currentRoom]["message"] += "\nThere is a graffiti with the label " + TextToSpray + " on the walls."
        Output = f"You sprayed {TextToSpray} against the walls"
        return Output

def TakeAction(IntendetUse, item, currentRoom, inventory):
    if IntendetUse == "read":
        Output = read(item)
    elif IntendetUse == "start":
        Output = startDevice(item, currentRoom, inventory)
    elif IntendetUse == "spray":
        Output = spray(item, currentRoom)
    elif IntendetUse == "cut":
        Output = cut(item, currentRoom, inventory)
    elif IntendetUse == "time":
        Output = GetTime(item)
    return Output

def startDevice(device, currentRoom, inventory):
    Output = ""

    if device == "computer":
        if currentRoom == "Server Room":

            logged_in = False
            admin_pass = "CoronaOutbreak2020"
            Password = input("[sudo] Password for admin: ")
            if Password == "script:passwd admin":
                admin_pass = input("Please enter the desired password: ")
                print("Password for admin changed")
                if input("[sudo] Password for admin: ") == admin_pass:
                    logged_in = True
                    achievements["Got into Server "] = True,
            elif Password == "CoronaOutbreak2020":
                print("Correct password")
                logged_in = True
                achievements["Got into Server "] = True,
            else:
                print("Wrong password")
                Output = ""
                sleep(1.5)

            # Create a command-line interface to allow the user to view, add, update, and delete data
            while logged_in:
                command = input("Enter a command (view, add, update, delete, list, or quit): ")
                if command == "view":
                    student_id = input("Schüler-ID: ")
                    if student_id in database:
                        student = database[student_id]
                        print(f"Name: {student['name']}")
                        print("Noten:")
                        for class_name, grade in student["grades"].items():
                            print(f"  {class_name}: {grade}")
                        print(f"Fehltage: {student['absences']} Tage")
                    else:
                        print("Schüler nicht gefunden.")
                elif command == "add":
                    name = input("Enter the student's name: ")
                    student_id = input("Schüler-ID: ")
                    add_student(name, student_id)
                elif command == "update":
                    student_id = input("Schüler-ID: ")
                    if student_id in database:
                        field = input("Welches Feld willst du verändern? (Noten oder Fehltage): ")
                    if field == "Noten":
                        class_name = input("Fach: ")
                        new_grade = input("Note: ")
                        update_grade(student_id, class_name, new_grade)
                        achievements["Changed a grade "] = True
                    elif field == "Fehltage":
                        new_absences = int(input("Anzahl der Fehlstunden: "))
                        update_absences(student_id, new_absences)
                    else:
                        print("Schüler nicht gefunden.")
                elif command == "delete":
                    student_id = input("Enter the student's ID number: ")
                    if student_id in database:
                        delete_student(student_id)
                    else:
                        print("Schüler nicht gefunden.")
                elif command == "list":
                    for student_id in database:
                        print(f"{student_id}: {database[student_id]['name']}")
                elif command == "quit":
                    logged_in = False
                    break
                else:
                    print("Invalid command.")
        else:
            Output = f"There is no computer in {currentRoom}"

    elif device == "laptop":
        loopControl = True
        while loopControl:
            move = ''
            while move == '': 
                print(colors.fg.green + '''
\033[04m\033[01mWelcome to your laptop\033[0m
Commands:
    read [file]
    copy [usbdrive]
    exit
''')        
                print("\n----------------------------------------------\n")
                print("files:\n")
                fileList = list(filesOnLaptop.keys())
                for item in fileList:
                    print('\033[34m' + item + '\033[0m')
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
                                Output = f"{colors.bold}{colors.underline}You are reading the file {file}{colors.reset}:\n" + filesOnLaptop[file]["content"]
                            else:
                                Output = f"{file} doesnt have any content"
                        else:
                            Output = f"{file} doesnt exist!"
                if move[0] == "copy":
                    if len(move) == 1:
                        Output = "You have to specify a usbdrive to copy"
                    else:
                        usbdrive = move[1]
                        if usbdrive == "usbstick":
                            if "usbstick" in inventory:
                                achievements["Copied USB      "] = True
                                Output = "You successfully copied the 2 files from the usbstick to your laptop\nYou can now read them."
                                filesOnLaptop.update({"grades.txt":{"content":grades_txt}})
                                filesOnLaptop.update({"abitur2011.txt":{"content":abitur_2011}})
                            else:
                                Output = f"You dont have {usbdrive} in your inventory"
                        else:
                            Output = f"You cant copy {usbdrive}"
                if move[0] == "exit":
                    typingEffect("Shutdown of laptop initiated...", 0.05)
                    loopControl = False

    else:
        Output = f"There is no device with the name {device} here"

    return Output
