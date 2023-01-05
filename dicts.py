rooms = {


            # Ground Level Outside
            'Building Entrance' : { 
                'south' : 'Park',
                'east'  : 'Eastern side',
                'west'  : 'Playground',
                'north' : 'Entrance',
                'message' : 'You stand infront of the big building entrance, the night is dark and silent...\n',
                'messageRead' : 0,
                },

            'Eastern side' : {
                  'west'  : 'Building Entrance',
                  'EnterableObjectDestination' : 'Classroom',
                  'message' : 'You go along the side of the building and you see a window a bit further up the wall, probably leading to a classroom.\nTip: You might have something to break it..\n',
                  'messageRead' : 0
            },
            'Playground' : {
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
                  'message' : 'You are in the front park of the Gymnasium Altona. You can hear a car pass by at the street every now and then...\nThere is a bike with a crusty old bikelock on it, you can use it to escape the scene,\nbut you will need something to force it open with.\n',
                  'messageRead' : 0
                },

            'Entrance' : {
                  'south'  : 'Building Entrance',
                  'message' : 'The big old door of the entrance towers up infront of you.\nThe inside of the building looks dark and scary..\n',
                  'door'  : "EntranceDoor",
                  'messageRead' : 0
                },     

            'Playground Window' : {
                'south' : 'Playground',
                'message' : 'The window is infront of you.\nYou can try to enter it, you might get lucky.\n',
                'messageRead' : 0,
                'EnterableObject'  : 'window',
                'EnterableObjectDestination' : 'Basement Window'
            },

            "Janitor stash" : {
                "east" : "Playground",
                "item" : ["boltcutters","entrancekey"],
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
                "east" : "Boys Bathroom",
                'message' : 'You go down the floor of the 5th graders, you remember the times\nwhen you had to walk through here everyday and endure the loud noises of the kids...\n',
                'messageRead' : 0
            },

            "Computer Room" : {
                "north" : "Office Hallway",
                "message": "You entered the computer room and you look around. There is a PC with a monitor attached and next to it are some drawers.\nYou can try to open the drawers.\n",
                "messageRead" : 0
            },

            "Classroom" : {
                "north" : "Ground Hallway",
                "message" : "You stand in the middle of this goofy classroom with pictures of students on the walls\nand those small little chairs that remind you of your early days in this school.\nThere is a closet next to the teachers desk, you can try to open it.\n",
                "item" : ["lunchbox"],
                "messageRead" : 0
            },

            'Office Hallway' : {
                'south' : 'Computer Room',
                'north' : 'Teachers Room',
                'west'  : 'Secretary Room',
                'east'  : 'Entrance Hall',
                'message' : 'You enter the Hallway that starts on the left side of the Entrance hall\nYou can see the entrance to multiple rooms.\n',
                'messageRead' : 0
            },

            "Secretary Room" : {
                "east" : "Office Hallway",
                "item" : ["classbook","letter"],
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

            "Boys Bathroom" : {
                "west" : "Ground Hallway",
                "item" : ["lighter", "weedbaggy"],
                "message" : "You enter the boys bathroom and it smells awfully like weed.\nEverything is dirty and toilet paper was thrown around.\n",
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
                "message" : "You see the big server light flickering, and right below it there stands the main computer which is connected to all the systems.\nYou can start the computer and try to get into it.\n",
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
                "message" : "You entered the small shop of the school in which the students buy their food.\nIt reminds you of the days you were a 5th grader and went here every break.\n",
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
                "burnable": True,
                "info": "The item letter has the usage 'read' and you can read it with either 'read letter' or 'use letter read'"
            },
            
            "paper" : {
                "use" : "read",
                "burnable": True,
                "info" : "The item paper has the usage 'read' and you can read it with either 'read paper' or 'use paper read'"
            },

            "encyclopedia" : {
                "use" : "read",
                "burnable": True,
                "info" : "The item encyclopedia has the usage 'read' and you can read it with either 'read encyclopedia' or 'use encyclopedia read'"
            },

            "watch" : {
                "use" : "time",
                "info" : "The item watch has the usage time and you can look up the time with either 'time' or 'use watch time'"
            },

            "worksheet" : {
                "use" : "read",
                "burnable": True,
                "info": "The item worksheet has the usage 'read' and you can read it with either 'read worksheet' or 'use worksheet read'"
            },

            "lunchbox" : {
                "info" : "The item lunchbox can be opened with 'open lunchbox'"
            },

            'laptop' : {
                "use" : "start",
                "info" : "The laptop has the usage 'start' and you can start it with either 'start laptop' or 'use laptop start'"
            },

            "lighter" : {
                "use" : "burn",
                "info" : "The lighter can be used to burn items with 'burn [item]'"
            },

            "weedbaggy" : {
                "burnable" : True,
                "info" : "This is just a weed baggy"
            }, 

            'matchbox'  :  {
                "use" : "burn",
                "info" : "The matchbox can be used to burn items with 'burn [item]'"
            },

            'graffitican'  : {
                "use" : "spray",
                "info" : "You can use the graffitican to make street art. Enter 'use graffitican spray' to use it"
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
                "burnable": True,
                "info" : "The item classbook has the usage 'read' and you can read it with either 'read classbook' or 'use classbook read'",
            },

            "stone" : {
                "throwable" : True,
                "info" : "You can use the item stone to throw at a window with the command 'throw stone'"
            },

            "boltcutters" : {
                "use" : "cut",
                "info" : "You can use the boltcutters to cut a lock with 'use boltcutters cut'",
            },

            "usbstick" : {
                "burnable": True,
                "info" : "You can copy the usbstick with your laptop. You can start it with 'start laptop'"
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
                "key" : "serverroomkey",
                "direction" : "north",
                "destination" : "Server Room"
            },

            'Principle Door' : {
                "direction"  : "west",
                "destination" : "Principles Office"
            }
}

grades_txt = """
Maria Schmidt - Mathematik: 2, Deutsch: 2, Englisch: 3
Hans Müller - Mathematik: 3, Deutsch: 3, Englisch: 4
Lena Weber - Mathematik: 4, Deutsch: 4, Englisch: 4
Max Schmitz - Mathematik: 3, Deutsch: 4, Englisch: 4
Sophie Bauer - Mathematik: 4, Deutsch: 3, Englisch: 3
Sarah Keller - Mathematik: 3, Deutsch: 2, Englisch: 2
Tom Weber - Mathematik: 2, Deutsch: 2, Englisch: 3
Anna Schmidt - Mathematik: 4, Deutsch: 4, Englisch: 5
Felix Müller - Mathematik: 4, Deutsch: 5, Englisch: 4
Marie Bauer - Mathematik: 4, Deutsch: 3, Englisch: 3
Peter Schmitz - Mathematik: 3, Deutsch: 3, Englisch: 4
Lena Keller - Mathematik: 4, Deutsch: 4, Englisch: 4
Max Weber - Mathematik: 3, Deutsch: 4, Englisch: 4
Sarah Müller - Mathematik: 4, Deutsch: 3, Englisch: 3
Tom Schmidt - Mathematik: 2, Deutsch: 2, Englisch: 3
Anna Bauer - Mathematik: 4, Deutsch: 4, Englisch: 5
Felix Schmitz - Mathematik: 4, Deutsch: 5, Englisch: 4
Marie Weber - Mathematik: 4, Deutsch: 3, Englisch: 3
Peter Keller - Mathematik: 3, Deutsch: 3, Englisch: 4
Lena Müller - Mathematik: 4, Deutsch: 4, Englisch: 4
Max Schmidt - Mathematik: 3, Deutsch: 4, Englisch: 4
Sarah Bauer - Mathematik: 4, Deutsch: 3, Englisch: 3
Tom Schmitz - Mathematik: 2, Deutsch: 2, Englisch: 3
Anna Keller - Mathematik: 4, Deutsch: 4, Englisch: 5
Felix Weber - Mathematik: 4, Deutsch: 5, Englisch: 4
Marie Müller - Mathematik: 4, Deutsch: 3, Englisch: 3
Peter Schmidt - Mathematik: 3, Deutsch: 3, Englisch: 4
Lena Schmitz - Mathematik: 4, Deutsch: 4, Englisch: 4
Max Keller - Mathematik: 3, Deutsch: 4, Englisch: 4
Sarah Weber - Mathematik: 4, Deutsch: 3, Englisch: 3
Tom Bauer - Mathematik: 2, Deutsch: 2, Englisch: 3
Anna Schmitz - Mathematik: 4, Deutsch: 4, Englisch: 5
Felix Müller - Mathematik: 4, Deutsch: 5, Englisch: 4
"""

abitur_2011 = """
Deutsch: https://gymaltona.de/secure/abitur/vertraulich/deutsch.pdf
Mathematik: https://gymaltona.de/secure/abitur/vertraulich/mathematik.pdf
Englisch: https://gymaltona.de/secure/abitur/vertraulich/englisch.pdf
Französisch: https://gymaltona.de/secure/abitur/vertraulich/französisch.pdf
Spanisch: https://gymaltona.de/secure/abitur/vertraulich/spanisch.pdf
Biologie: https://gymaltona.de/secure/abitur/vertraulich/biologie.pdf
Chemie: https://gymaltona.de/secure/abitur/vertraulich/chemie.pdf
Physik: https://gymaltona.de/secure/abitur/vertraulich/physik.pdf
Geschichte: https://gymaltona.de/secure/abitur/vertraulich/geschichte.pdf
Geographie: https://gymaltona.de/secure/abitur/vertraulich/geographie.pdf
Politikwissenschaft: https://gymaltona.de/secure/abitur/vertraulich/politikwissenschaft.pdf
Philosophie: https://gymaltona.de/secure/abitur/vertraulich/philosophie.pdf
Kunst: https://gymaltona.de/secure/abitur/vertraulich/kunst.pdf
Musik: https://gymaltona.de/secure/abitur/vertraulich/musik.pdf
Sport: https://gymaltona.de/secure/abitur/vertraulich/sport.pdf
"""

database = {
    "1": {"name": "Jacob", "grades": {"Deutsch": 3, "Mathematik": 4, "Englisch": 3, "Geschichte": 1}, "absences": 190},
    "2": {"name": "Julius", "grades": {"Deutsch": 1, "Mathematik": 1, "Englisch": 2, "Geschichte": 2}, "absences": 2},
    "3": {"name": "Vincent", "grades": {"Deutsch": 2, "Mathematik": 1, "Englisch": 1, "Geschichte": 3}, "absences": 0},
    "4": {"name": "Ilhan", "grades": {"Deutsch": 2, "Mathematik": 2, "Englisch": 3, "Geschichte": 2}, "absences": 3},
    "5": {"name": "Yasin", "grades": {"Deutsch": 3, "Mathematik": 1, "Englisch": 2, "Geschichte": 3}, "absences": 1},
    "6": {"name": "Philip", "grades": {"Deutsch": 3, "Mathematik": 2, "Englisch": 3, "Geschichte": 1}, "absences": 2},
    "7": {"name": "Lucie", "grades": {"Deutsch": 3, "Mathematik": 3, "Englisch": 4, "Geschichte": 2}, "absences": 0},
    "8": {"name": "Cem", "grades": {"Deutsch": 4, "Mathematik": 1, "Englisch": 3, "Geschichte": 3}, "absences": 3},
    "9": {"name": "Chiara Keskiner", "grades": {"Deutsch": 4, "Mathematik": 2, "Englisch": 4, "Geschichte": 1}, "absences": 1},
    "10": {"name": "Paul", "grades": {"Deutsch": 4, "Mathematik": 3, "Englisch": 4, "Geschichte": 2}, "absences": 2},
    "11": {"name": "Janis", "grades": {"Deutsch": 5, "Mathematik": 1, "Englisch": 4, "Geschichte": 3}, "absences": 0},
    "12": {"name": "Vicente", "grades": {"Deutsch": 5, "Mathematik": 2, "Englisch": 5, "Geschichte": 1}, "absences": 3},
    "13": {"name": "Inan", "grades": {"Deutsch": 5, "Mathematik": 2, "Englisch": 5, "Geschichte": 2}, "absences": 1},
}

filesOnLaptop = {
            'passwordbypass.txt' : {
                "content"   : '''
This is a tutorial on how to bypass security on LinuxMint computers
1. Start the computer
2. enter "script:adduser bypass" as the password
3. Click on login
4. change the username to bypass and leave the password blank
5. Login

Done!
''',
            },

}

achievements = {
    "Copied USB      ": False,
    "Unlocked safe   ": False,
    "Got into Server ": False,
    "Changed a grade ": False,
}
