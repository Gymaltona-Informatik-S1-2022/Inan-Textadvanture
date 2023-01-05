#!/bin/python3
from usages import *
from functions import *
from dicts import *
import sys
import os
import readline

cls() # Clear the screen

#-----------------------------Settings------------------------------------#
TypingSpeed = 0.02
currentRoom = 'Building Entrance' # Define Starting room
#-----------------------------Start Variables-----------------------------#

timer_start()
# Declare start variables
Output = ""
# Create inventory list and add start items
inventory = []
inventory += ["laptop"]
# InstructionsShown
InstructionsShown = 0
# Current floor
currentFloor = 0
# Last Room
lastRoom = ""
# Variables to prevent glitches
drawers = False
WindowShattered = False
closet = False

# function to print the current status to player
def showStatus():
  print('\033[96m------------Room Info---------------', colors.reset)
  print('Your current position is the ' + colors.fg.orange + currentRoom + colors.reset + "\n")
  room = rooms[currentRoom]
  if room['messageRead'] != 1:
    typingEffect(room["message"], TypingSpeed)
    room['messageRead'] += 1
  else:
    print(room['message'])
  # Print the current items inside inventory
  InventoryMessage = ', '.join(inventory)
  print('\n\033[33mInventory: ' + colors.reset + InventoryMessage,)
  # Print all items in room 
  if "item" in rooms[currentRoom]:
    if rooms[currentRoom]["item"] != []:
      print('You see a ' + " and a ".join(rooms[currentRoom]['item']))
  print('\033[96m-------------Output-----------------', colors.reset)
  # Print output if there is one
  print(f"\n{Output}")



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
  len_WtoE = 9

  vert_line = "|"
  hzt_line = "-- W -- X -- E --"
  print("")
  print(north.center(18 + len(west)*2))
  print("")
  print(vert_line.center(18 + len(west)*2))
  print(n.center(18 + len(west)*2))
  print(vert_line.center(18 + len(west)*2))
  print(west + hzt_line.center(20 - len(west) * 2) + east)
  print(vert_line.center(18 + len(west)*2))
  print(s.ljust(9 + len(west), " ")[::-1][:-len(s)] + s)
  print(vert_line.center(18 + len(west)*2))
  print("")
  print(south.center(18 + len(west)*2))
  print("")

# Loop forever (unless exit)
while True:
  if InstructionsShown == 0:
    showInstructions()
    InstructionsShown = 1
  else:
    cls()
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

  if move[0] == "unlock":
    object = move[1]
    Output = input("Please enter the 4 digit pin for the safe\n")
    if Output != "1882":
      Output = "Safe didn't open. Look around closely in the previous rooms, maybe you can find a hint.\n"
    else:
      Output = "Safe opened\nIt would be smart to not just steal the things, but bring them back here after you are done."
      achievements["Unlocked safe   "] = True
      rooms[currentRoom]["message"] = rooms[currentRoom]["message"][:69]
      if "item" in rooms[currentRoom]:
        rooms[currentRoom]["item"] += ["serverroomkey"]
      else:
        rooms[currentRoom]["item"] = ["serverroomkey"]
  
  if move[0] == "drop":
    if len(move) == 1:
      Output = "You have to specify an item to drop"
    else:
      item = move[1]
      try:
        inventory.remove(item)
        try:
          rooms[currentRoom]["item"] += [item]
        except:
          rooms[currentRoom]["item"] = [item]
        Output = f"You dropped the {item}"
      except:
        Output = f"You dont have {item} in your inventory"


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
            Output = TakeAction(IntendetUse, item, currentRoom, inventory)

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
      lastRoom = currentRoom
      currentRoom = rooms[currentRoom][move[1]]
      rooms["Stairs"]["south"] = lastRoom
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  # If user types "get"
  if move[0] == 'get' :
    # If the current room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']: 
      inventory += [move[1]] # Add the item to the inventory
      Output = move[1] + ' got!' + "\n" + items[move[1]]["info"] # Display output that item was received
      rooms[currentRoom]['item'].remove(move[1]) # Delete the item from the room so it can't be taken twice
    else:
      # If item doesnt exist print an error
      Output = "Can\'t get " + move[1] + "! Item doesn't exist in this room"

  if move[0] == "eat":
    if len(move) == 1:
      Output = "You have to specify the food that you want to eat"
    else:
      food = move[1]
      if food in inventory:
        if "food" in items[food]:
          Output = f"You have eaten the {food}"
          inventory.remove(food)
        else:
          Output = food + " is not eatable"
      else:
        Output = f"{food} is not in your inventory"
  
  if move [0] == "drink":
    if len(move) == 1:
      Output = "You have to specify the drink that you want to drink"
    else:
      drink = move[1]
      if drink in inventory:
        if "drink" in items[drink]:
          Output = f"You have drunken the {drink}"
          inventory.remove(drink)
        else:
          Output = drink + " is not drinkable"
      else:
        Output = f"{drink} is not in your inventory"

  # If user types "enter"
  if move[0] == "enter":
    if len(move) == 1:
      Output = "You have to specify the object that you want to enter"
    else:
      object = move[1]
      try:
        objectsInRoom = rooms[currentRoom]["EnterableObject"]
        if object in objectsInRoom: # Check if enterable object exists in room
          Destination = rooms[currentRoom]["EnterableObjectDestination"]
          chance = fifty_fifty() # Create a 50/50 chance if user can enter the object
          if currentRoom == "Playground Window":
            if chance == 1:
              currentRoom = Destination # if user is lucky let him enter the object
              try:
                currentFloor = rooms[currentRoom]["newfloorlevel"]
              except:
                  i = 1
            else:
              Output = f"Sadly you were out of luck and failed entering {object}"
          else:
            currentRoom = Destination # let the user enter the object
      except:
        Output = "This room has no enterable object"

  # If user types "start"
  if move[0] == "start":
    if len(move) == 1:  # Check if user specified an target device
      Output = "You have to specify the device that you want to start"
    else:
      # Start the specified device
      device = move[1]
      startDevice(device, currentRoom, inventory)

  # If user types "open"
  if move[0] == "open":
    if len(move) == 1: # Check if user specified door to open
      Output = "You have to specify the object that you want to open"
    else:
      if move[1] == "door":
        door = move[1]
        if door in rooms[currentRoom]: # check if current room has a door
          whichDoor = rooms[currentRoom]["door"] # Store the attributes of the door in a list
          if "key" in doors[whichDoor]: # Check if door needs a key
            KeyNeeded = doors[whichDoor]["key"] # store key-name in a variable
            if KeyNeeded in inventory: # Check if suer has the specific key
              Output = openDoor(currentRoom, whichDoor) # Open the door
            else:
              Output = f"You need the {KeyNeeded} to open the door"
          else:
            Output = openDoor(currentRoom, whichDoor) # Open door if it doesnt need a key
        else:
          Output = "There is no door in this area"
      elif move[1] == "lunchbox":
        if "lunchbox" in inventory:
          Output = "You open the lunchbox and see a dirty sandwhich full of mold"
        else:
          Output = "You don't have the item lunchbox"  
      elif move[1] == "closet":
        if currentRoom == "Classroom":
          if closet == False:
            closet = True
            Output = "You open the closet of the classroom and in it are several encyclopedias aswell as a quite expensive looking watch"
            try: 
              rooms["Classroom"]["item"] += ["encyclopedia","watch"]
            except:
              rooms["Classroom"]["item"] = ["encyclopedia","watch"]
          else:
            Output = "You open the closet of the classroom but nothing interesting is inside it"
        else:
          Output = "There is no closet in this room"
      elif move[1] == "drawers":
        if currentRoom == "Computer Room":
          if drawers == False:
            drawers = True
            Output = "You open the drawers and in one of them lays a paper with text written on it"
            if "item" in rooms["Computer Room"]:
              rooms["Computer Room"]["item"] += ["paper"]
            else:
              rooms["Computer Room"]["item"] = ["paper"]
          else:
            Output = "You open the drawers but nothing is inside"
        else:
          Output = "There are no drawers in this room"
      else:
        Output = f"You can't open a {move[1]}"

  # If user types "info"
  if move[0] == "info":
    if len(move) == 1: # Check if user specified item
      Output = "You have to specify the item that you want info for"
    else:
      item = move[1]
      if item in inventory: # Check if user has item in inventory
        Output = getinfo(item) # Get info of item
      else: 
        Output = f"You dont have {item} in your inventory"

  if move[0] == "up":
    if currentRoom == "Stairs":
      if currentFloor == -1:
        currentRoom = "Ground Hallway"
        currentFloor += 1
        Output = "You walked up the stairs"
      elif currentFloor == 0:
        currentRoom = "nothing"
        currentFloor += 1
        Output = "You walked up the stairs"
      else:
        Output = "You cant go up here"
    else:
      Output = "You cant go up here"

  if move[0] == "down":
    if currentRoom == "Stairs":
      if currentFloor == 0:
        currentRoom = "Eastern Basement Hallway"
        currentFloor -= 1
        Output = "You walked down the stairs"
      elif currentFloor == 1:
        currentRoom = "Ground Hallway"
        currentFloor -= 1
        Output = "You walked down the stairs"
      else:
        Output = "You cant go down here"
    Output = "You cant go down here"
  
  if move[0] == "throw":
    if currentRoom == "Eastern side":
      if WindowShattered == False:
        if len(move) == 1:
          Output = "You have to specify an item to throw"
        else:
          item = move[1]
          if "throwable" in items[item]:
            inventory.remove(item)
            WindowShattered = True
            rooms["Eastern side"]["EnterableObject"] = "window"
            Output = f"You threw the {item} at the window and it shattered.\nYou can now enter it\n"
            rooms["Eastern side"]["message"] = "You go along the side of the building and you see an open shattered window a bit further up the wall, probably leading to a classroom."
          else:
            Output = f"You cannot throw a {item}"
      else:
        Output = "You can't throw at anything in this room"
    else:
      Output = "There is nothing to throw at in this room"

  if move[0] == "burn":
    if len(move) == 1:
      Output = "You have to specify an item to burn"
    else:
      item = move[1]
      if item in inventory:
        for i in inventory:
          if items[i].get("use") == "burn":
            if items[item].get("burnable") == True:
              Output = f"You burned {item}"
              inventory.remove(item)
            else:
              Output = f"You cant burn {item}"
            break
          else:
            Output = "You dont have any item in your inventory to burn something with."
      else:
        Output = f"You dont have {item} in your inventory"
      
  if move[0] == "time":
    Output = GetTime("watch", inventory)

  # If user types "help"
  if move[0] == "help":
    Output = showInstructions() # Show user game instructions


  # If user types "exit"
  if move[0] == 'exit':
    words = "Exiting..."
    typingEffect(words, 0.05) # Display exit message with typing effect
    sys.exit("") # Exit program
