#!/bin/python3
from usages import *
from functions import *
from dicts import *
import sys

# Declare start variables
Output = ""
# Create inventory list and add start items
inventory = []
inventory += ["laptop"]
# Define Starting room
currentRoom = 'Building Entrance'

# function to print the current status to player
def showStatus():
  print('---------------------------')
  print('Your current position is the ' + currentRoom + "\n")
  room = rooms[currentRoom]
  if room['messageRead'] != 1:
    typingEffect(room["message"], 0.02)
    room['messageRead'] += 1
  else:
    print(room['message'])
  # Print the current items inside inventory
  print('\nInventory : ' + str(inventory))
  # Print all items in room
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "item2" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item2'])
  print("---------------------------")
  # Print output if there is one
  print(f"{Output}")



# Displays a map of all the accesable rooms from the current room
def room_map():
  global message
  # All variable defaults should be blank, and only be filled if the directin value exists in current room
  try:
    north = rooms[currentRoom]['north']
  except:
    north = ""
  try:
    south = rooms[currentRoom]['south']
  except:
    south = ""
  try:
    east = rooms[currentRoom]['east']
  except:
    east = ""
  try:
    west = rooms[currentRoom]['west']
  except:
    west = ""

  # Print the map
  n = "N"
  s = "S"
  vert_line = "|"
  hzt_line = "-- W -- X -- E --"
  print(north.center(40))
  print("")
  print(vert_line.center(40))
  print(n.center(40))
  print(vert_line.center(40))
  print(west + hzt_line.center(40 - len(west) * 2) + east)
  print(vert_line.center(40))
  print(s.center(40))
  print(vert_line.center(40))
  print("")
  print(south.center(40))
  print("")

showInstructions()

# Loop forever (unless exit)
while True:
  room_map()
  showStatus()
  Error = ""
  Output = ""

  # Get the players input and display a small > at the beginning of the commandline
  move = ''
  while move == '':  
    move = input('>')

  # Break all the input parameters into an array with .split()
  move = move.lower().split()
 
  # Define what happens when user uses the function "read"
  if move[0] == 'read':
    if len(move) == 1:
      Output = "You have to specify the item that you want to read"
    else:
      item = move[1]
      if hasItem(inventory, item):
        itemproperties = dict(items[item])
        if items[item]['use'] == "read":
          Output = read(item)
        else:
          Output = f"{item} can't be read"
      else:
        Output = f"You dont have {item}"

  # Define what happens when user uses the function "use"  
  if move[0] == 'use':
    item = move[1]
    if hasItem(inventory, item):
      ItemDict = dict(items[item])
      if "use" in ItemDict:
        if len(move) == 2:
          Output = "You didnt specify the usage of the item\n use [item] [usage]"
        else:
          IntendetUse = move[2]
          itemproperties = dict(items[item])
          usages = items[item]['use'].split(' ')
          hasUse = hasItem(usages, IntendetUse)
          if hasUse:
            #Output = f"{item} can be used to {IntendetUse}"
            Output = TakeAction(IntendetUse, item)

          else:
            Output = f"{item} can't be used to {IntendetUse}"
      else:
        Output = f"{item} doesnt have any usages"
    else:
      Output = f"Error: You dont have the item {item} in your inventory"
    

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  # If user types "get"
  if move[0] == 'get' :
    # If the current room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']: 
      inventory += [move[1]] # Add the item to the inventory
      Output = move[1] + ' got!' # Display output that item was received
      del rooms[currentRoom]['item'] # Delete the item from the room so it can't be taken twice
    elif "item2" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item2']: #add the item to their inventory
      inventory += [move[1]] # Add the item to the inventory
      Output = move[1] + ' got!' # Display output that item was received
      del rooms[currentRoom]['item2'] # Delete the item from the room so it can't be taken twice
    else:
      # If item doesnt exist print an error
      Output = "ERROR: Can\'t get " + move[1] + "! Item doesn't exist"

  # If user types "enter"
  if move[0] == "enter":
    if len(move) == 1: # Check if user specified an target object
      Output = "You have to specify the object that you want to enter"
    else:
      object = move[1]
      objectsInRoom = rooms[currentRoom]["EnterableObject"]
      if object in objectsInRoom: # Check if enterable object exists in room
        Output = f"The room has {object}"
        Destination = rooms[currentRoom]["EnterableObjectDestination"]
        chance = fifty_fifty()
        if chance == 1:
          currentRoom = Destination
        else:
          Output = f"Sadly you were out of luck and failed entering {object}"

  if move[0] == "start":
    if len(move) == 1:
      Output = "You have to specify the device that you want to start"
    else:
      device = move[1]
      startDevice(device)

  if move[0] == "open":
    if len(move) == 1:
      Output = "You have to specify the door that you want to open"
    else:
      door = move[1]
      if door in rooms[currentRoom]:
        whichDoor = rooms[currentRoom]["door"]
        if "key" in doors[whichDoor]:
          KeyNeeded = doors[whichDoor]["key"]
          if KeyNeeded in inventory:
            Output = openDoor(currentRoom, whichDoor)
          else:
            Output = f"You need the {KeyNeeded} to open the door"
        else:
          Output = openDoor(currentRoom, whichDoor)
      else:
        Output = "There is no door in this area"

  if move[0] == "help":
    Output = showInstructions()



  if move[0] == 'exit':
    words = "Exiting..."
    typingEffect(words, 0.05)
    sys.exit("")
