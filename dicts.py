rooms = {


            # Ground Level Outside
            'Building Entrance' : { 
                'south' : 'Park',
                'east'  : 'Eastern side',
                'west'  : 'Playround',
                'north' : 'Entrance',
                'message' : 'You stand infront of the big building entrance, the night is dark and silent...\n',
                'messageRead' : 0,
                'item'  : ['letter',"entrancekey"],
                },

            'Eastern side' : {
                  'north' : 'Hall',
                  'east'  : 'Living Room',
                  'message' : '',
                  'messageRead' : 0
            },
            'Playround' : {
                  'east' : 'Building Entrance',
                  "north" : "Playground Window",
                  "west"  : "Janitor stash",
                  'item'  : ["matchbox"],
                  'message' : 'You are in the middle of the small playground on the left side.\nThere is a small window a bit further infront of you, light seems to shine out of it.\n',
                  'messageRead' : 0
                },

            'Park' : {
                  'north' : 'Building Entrance',
                  'item'  : ["stone"],
                  'message' : 'You are in the front park of the Gymnasium Altona. You can hear a car pass by at the street every now and then...\n',
                  'messageRead' : 0
                },

            'Entrance' : {
                  'south'  : 'Building Entrance',
                  'message' : 'The big old door of the entrance towers up infront of you.\nThe inside of the building looks dark and scary..\n',
                  'door'  : "EntranceDoor",
                  'messageRead' : 0
                },     

            'Playground Window' : {
                'south' : 'Playround',
                'message' : 'The window is infront of you.\nYou can try to enter it, you might get lucky.\n',
                'messageRead' : 0,
                'EnterableObject'  : 'window',
                'EnterableObjectDestination' : 'Basement Window'
            },

            "Janitor stash" : {
                "east" : "Playground",
                "item" : ["boltcutters"],
                "message" : "You open the slightly open door and find yourself in this dark and narrow room full of tools.\n",
                "messageRead" : 0
            },

            # Ground Level Inside
            'Entrance Hall' : {
                'east'  : 'Ground Hallway',
                'south' : 'Entrance',
                'west'  : 'Office Hallway',
                'message' : 'The entrance hall is big and has high walls, you look around you and there are hallways on your sides.\n',
                'messageRead' : 0
            },

            "Ground Hallway" : {
                "west" : "Entrance Hall",
                "north" : "Stairs",
                "south" : "Classroom",
                'message' : 'You go down the floor of the 5th graders, you remember the times\nWhen you had to walk through here everyday and endure the loud noises of the kids...\n',
                'messageRead' : 0
            },

            "Classroom" : {
                "north" : "Ground Hallway",
                "message" : "",
                "item" : ["lunchbox"],
                "messageRead" : 0
            },

            'Office Hallway' : {
                'south' : 'Ground level computerroom',
                'north' : 'Teachers Room',
                'west'  : 'Secretary Room',
                'east'  : 'Entrance Hall',
                'message' : 'You enter the Hallway that starts on the left side of the Entrance hall\nYou can see the entrance to multiple rooms.\n',
                'messageRead' : 0
            },

            "Secretary Room" : {
                "east" : "Office Hallway",
                "item" : ["classbook"],
                "message" : "There is a desk with a bunch of papers and a mounted telephone.\nHere you always went when you wanted to fake a illness to go home from school.\n",
                "messageRead" : 0
            },

            'Teachers Room'  : {
                'south' : 'Office Hallway',
                'door'  : 'Principle Door',
                "item"  : ["worksheet"],
                'messageRead'  : 0,
                'message' : 'You enter the teachers room, the door was wide open and you look around you.\nLeft of you, you can see a door, you look at the label and it says "Principles Room"\n'
            },
            "Principles Office" : {
                "east"  : "Teachers Room",
                "message"  : "There is a desk infront of you, on it there are many sheets of paper.\nNext to the desk is a safe with a number lock on it\n",
                "item" : ["usbstick"],
                "messageRead"  : 0
            },

            "Stairs" : {
                "south" : "",
                "message": "You can walk down/up on these stairs with the commands 'down' and 'up'\n",
                "messageRead" : 0
            },


            # Basement Level

            'Basement Window' : {
                  'north' : 'Northern Basement Hallway',
                  "east"  : "Eastern Basement Hallway",
                  "door"  : "StorageroomDoor",
                  "newfloorlevel" : -1,
                  'message' : 'WOOOMS! You climbed into the window and fell down on the floor.\nYou stand up and look around you, everywhere is darkness except a small white light flickering on the other side of the room...\nSouthern of you is a old looking door.\n',
                  'messageRead' : 0
            }, 

            'Northern Basement Hallway' : {
                  'south' : 'Basement Window',
                  'door' : 'ServerRoomDoor',
                  'message' : 'You continue along the basement hallway and you can merely see the outline of a door northern of you and lights flashing under the door.\n',
                  'messageRead' : 0
            } ,

            'Basement Storage Room'  : {
                'north' : 'Basement Window',
                'item'  : ["graffitican"],
                'message' : 'You enter the room and you can feel that not many people come around here, everything is dusty and dark.\n',
                'messageRead' : 0
            },

            "Server Room" : {
                "south" : "Northern Basement Hallway",
                "message" : "You see the big server light flickering, and right below it there stands the main computer which is connected to all the systems.\n",
                "messageRead" : 0
            },

            "Eastern Basement Hallway" : {
                "south"  : "Saftladen",
                "west"   : "Basement Window",
                "north"  : "Stairs",
                "message" : "You continue along the hallway and you can see graffiti made by students all around you.\n",
                "messageRead" : 0
            },

            "Saftladen" : {
                "north" : "Eastern Basement Hallway",
                "west"  : "Saftladen Kitchen",
                "message" : "You entered the small shop of the school in which the students buy their food, it reminds you of the days you were a 5th grader and went here every break.\n",
                "messageRead" : 0
            },

            "Saftladen Kitchen" : {
                "east" : "Saftladen",
                "message" : "You stand between the prezels and drinks in the kitchen of the shop.\n",
                "item" : ["apple"],
                "messageRead" : 0
            },
            

         }

items = {    
            'letter' : {
                "use" : "read",
                "info": "The item letter has the usage 'read' and you can read it with either 'read letter' or 'use letter read'"
            },

            "worksheet" : {
                "use" : "read",
                "info": "The item worksheet has the usage 'read' and you can read it with either 'read worksheet' or 'use worksheet read'"
            },

            "lunchbox" : {
                "info" : "The item lunchbox can be opened with 'open lunchbox'"
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
            },

            "serverroomkey" : {
                "use" : "open",
                "doors" : "ServerRoomDoor",
                "info" : "The serverroomkey can be used to open the door to the Server Room"
            },

            "apple" : {
                "food" : True,
                "info" : "The apple can be eaten with 'eat apple'"
            },

            "beer" : {
                "drink" : True,
                "info" : "The beer can be drunken with 'drink beer'"
            },

            "classbook" : {
                "use" : "read",
                "info" : "The item classbook has the usage 'read' and you can read it with either 'read classbook' or 'use classbook read'",
            },

            "usbstick" : {
                ""
            }
}


doors = {
            'EntranceDoor' : {
                "key" : "entrancekey",
                "direction" : "north",
                "destination" : "Entrance Hall"
            },

            'StorageroomDoor' : {
                "direction" : "south",
                "destination" : "Basement Storage Room",
            },

            "ServerRoomDoor" : {
                "key" : "ServerRoomKey",
                "direction" : "north",
                "destination" : "Server Room"
            },

            'Principle Door' : {
                "direction"  : "west",
                "destination" : "Principles Office"
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
