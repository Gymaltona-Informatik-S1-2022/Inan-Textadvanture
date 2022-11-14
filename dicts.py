rooms = {


            # Ground Level Outside
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
                  'east' : 'Building Entrance',
                  'north'  : 'Playground Window',
                  'item'  : 'matchbox',
                  'message' : 'You are in the middle of the small playground on the left side.\nThere is a small window a bit further infront of you, light seems to shine out of it.',
                  'messageRead' : 0
                },

            'Park' : {
                  'north' : 'Building Entrance',
                  'west'  : 'Playground',
                  'east'  : 'Street',
                  'item'  : 'flashlight',
                  'message' : 'You are in the front park of the Gymnasium Altona. You can hear a car pass by at the street every now and then...\n',
                  'messageRead' : 0
                },

            'Entrance' : {
                  'south'  : 'Building Entrance',
                  'message' : 'The big old door of the entrance towers up infront of you. The inside of the building looks dark and scary..',
                  'door'  : "EntranceDoor",
                  'messageRead' : 0
                },     

            'Playground Window' : {
                'south' : 'Playround',
                'message' : 'The window is infront of you.\nYou can try to enter it, you might get lucky',
                'messageRead' : 0,
                'EnterableObject'  : 'window',
                'EnterableObjectDestination' : 'Basement Window'
            },

            # Ground Level Inside
            'Entrance Hall' : {
                  'west'  : 'Dining Room',
                  'message' : 'You are in the foyer',
                  'messageRead' : 0
            },


            # Basement Level

            'Basement Window' : {
                  'north' : 'Northern Basement Hallway',
                  'message' : 'WOOOMS! You climbed into the window and fell down on the floor.\nYou stand up and look around you, everywhere is darkness except a small white light flickering on the other side of the room...',
                  'messageRead' : 0
            }, 

            'Northern Basement Hallway' : {
                  'south' : 'Basement Window',
                  'message' : 'You continue along the basement hallway and you can merely see the outline of a door eastern of you',
                  'door'  : 'StorageroomDoor',
                  'messageRead' : 0
            } ,

            'Basement Storage Room'  : {
                'west' : 'Northern Basement Hallway',
                'item'  : 'graffitican',
                'message' : '',
                'messageRead' : 0
            }
            

         }

items = {    
            'letter' : {
                "use" : "read",
                "info": "The item letter has the usage 'read' and you can read it with either 'read letter' or 'use letter read'"
            },

            'laptop' : {
                "use" : "start",
                "info" : "The laptop has the usage 'start' and you can start it with either 'start laptop' or 'use laptop start'"
            },

            'flashlight' : {
                "use" : "start",
                "info" : "The flashlight has the usage 'start' and you can start it with either 'start flashlight' or 'use flashlight start'"
            },           

            'matchbox'  :  {
                "use" : "light",
                "info" : ""
            },

            'graffitican'  : {
                "use" : "spray",
                "info" : "You can use the graffiti can to make street art. Enter 'use graffitican spray' to use it"
            },

            'entrancekey' : {
                "use" : "open",
                "doors" : "Entrance",
                "info"  : "The entrancekey can be used to open the Entrance door"
            }
}

doors = {
            'EntranceDoor' : {
                "key" : "entrancekey",
                "direction" : "north",
                "destination" : "Entrance Hall"
            },

            'StorageroomDoor' : {
                "direction" : "east",
                "destination" : "Basement Storage Room",
                "item"  : "graffitican"
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
