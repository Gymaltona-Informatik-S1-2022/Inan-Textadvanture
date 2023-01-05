from time import sleep
from dicts import *
import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

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

def getinfo(item):
    Output = items[item]["info"]
    return Output

def showInstructions():
  #print a main menu and the commands
  text = '''
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
  info [item]
  help
  exit
'''
  print(text)

  Output = text
  return Output

class colors:
  reset = '\033[0m'
  bold = '\033[01m'
  disable = '\033[02m'
  underline = '\033[04m'
  reverse = '\033[07m'
  strikethrough = '\033[09m'
  invisible = '\033[08m'

  class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'
  class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
