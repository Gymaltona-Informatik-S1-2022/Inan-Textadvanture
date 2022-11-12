rooms = {

            'Building Entrance' : { 
                  'south' : 'Park',
                  'east'  : 'Eastern side',
                  'west'  : 'Playround',
                  'north' : 'Entrance',
                  'message' : 'You stand infront of the big building entrance, the night is dark and silent...',
                  'messageRead' : 0,
                  'item'  : 'letter',
                  'item2' : 'entrancekey'
                },

            'Eastern side' : {
                  'north' : 'Hall',
                  'east'  : 'Living Room',
                  'item'  : 'knife',
                  'message' : '',
                  'messageRead' : 0
                },
            'Playround' : {
                  'south' : 'Building Entrance',
                  'east'  : 'Playground Window',
                  'item'  : 'matchbox',
                  'message' : 'You are in the middle of the small playground on the left side.\nThere is a small window on the side of the building east of you, light seems to shine out of it.',
                  'messageRead' : 0
                },
            'Playground Window' : {
                  'west' : 'Playround',
                  'message' : 'The window is infront of you.\nYou can try to enter it, you might get lucky',
                  'messageRead' : 0,
                  'EnterableObject'  : 'window',
                  'EnterableObjectDestination' : 'Basement Window'
                },
            'Basement Window' : {
                  'message' : 'WOOOMS!>>> You climbed into the window and fell down on the floor.\nYou stand up and look around you, everywhere is nothing but darkness...',
                  'messageRead' : 0
                }, 
            'Entrance' : {
                  'south'  : 'Building Entrance',
                  'message' : 'The big old door of the entrance towers up infront of you. The inside of the building looks dark and scary..',
                  'door'  : "EntranceDoor",
                  'messageRead' : 0
                },     

            'Entrance Hall' : {
                  'west'  : 'Dining Room',
                  'message' : 'You are in the foyer',
                  'messageRead' : 0
            }

         }

items = {
            'knife' : { 
                "use" : "hit cut",
                "damage" : 5
            },

            'key' : { 
                "use" : "",
            },      

            'letter' : {
                "use" : "read",
            },

            'laptop' : {
                "use" : "start"
            },

            'entrancekey' : {
                "use" : "open",
                "doors" : "Entrance"
            }
}

doors = {
            'EntranceDoor' : {
                "key" : "entrancekey",
                "direction" : "north",
                "destination" : "Entrance Hall"
            }
}

filesOnLaptop = {
            'passwordbypass.txt' : {
                "content"   : '''
This is a tutorial on how to bypass security on LinuxMint computers
1. Start the computer
2. enter the username "root"
3. enter "adduser bypass" as the username
4. Click on login
5. change the username to bypass and leave the password blank
6. Login

Done!
''',
                "isProgram" : 0
            },
            'trojan'  : {
                "isProgram" : 1,
                "connected" : 0
            }

}