from time import sleep
from dicts import *
import random

def typingEffect(text, interval):
  for char in text:
    sleep(interval)
    print(char, end='', flush=True)

def fifty_fifty():
    "Return 0 or 1 with 50% chance for each"
    return random.randrange(2)

def hasItem(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
    return False

def openDoor(currentRoom, whichDoor):
    DestinationDirection = doors[whichDoor]["direction"]
    Destination = doors[whichDoor]["destination"]
    rooms[currentRoom][DestinationDirection] = Destination
    Output = f"The door to the {Destination} opened, you can now proceed {DestinationDirection} to walk through it."
    return Output

def showInstructions():
  #print a main menu and the commands
  print('''
Text Advanture by Inan Salar
========

You are a student at the Gymnasium Altona. Your Abitur Exams are soon and your goal is to break into the Building,
steal the USB of the principle and make a copy of it.
But beware of the janitor!

Commands:
  go [direction]
  get [item]
  use [item] [purpose]
  read [item]
  open [door]
  enter [object]
  start [device]
''')

  Output = '''
Text Advanture
========

Get to the Garden with a key, a knife and a matchbox
But beware of the monsters!

Commands:
  go [direction]
  get [item]
  use [item] [purpose]
  read [item]
  open [door]
  start [device]
  enter
'''
  return Output