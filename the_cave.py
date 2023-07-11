import pyfiglet
import os
from time import sleep
import sys

def print_line(line):
    for char in line:
        print(char, end='', flush=True)
        sleep(0.05)
    #print("\n")


ascii_banner = pyfiglet.figlet_format("The Cave")
print(ascii_banner)
string_1 = ("Welcome to The Cave! You have fallen into a cave in a remote location and must find your way out. You have a limited amount of time to escape before you run out of supplies. Good luck!")
print_line(string_1)
input()
input("You will be able to move around the cave by typing 'go' and then the direction you want to go in. For example, 'go north' or 'go south'.")
#input("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
#input("You can pick up items by typing 'take' and then the name of the item. For example, 'take torch'.")
#input("You can drop items by typing 'drop' and then the name of the item. For example, 'drop torch'.")
#input("You can use items by typing 'use' and then the name of the item. For example, 'use torch'.")
#input("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.")
#input("You can type 'quit' to quit the game at any time.")
#input("You can type 'save' to save the game at any time.")
#input("You can type 'load' to load the game at any time.")
#input("You can type 'restart' to restart the game at any time.")
#input("You can type 'reset' to reset the game at any time.")
input("Press enter to begin.")
os.system('cls')

opening_banner = pyfiglet.figlet_format("Welcome to the Cave!")
print(opening_banner)
sleep(1)
string_2 = "You wake up in a dim cave. You can't remember how you got here or where you are. You can't see anything, but you can feel something in your pocket."
print_line(string_2)
sleep(1)
input("You take the item out of your pocket and feel it. It's a torch! You can use this to see in the dark. You light the torch and look around.")
input("You are lying in the centre of a large cavern, with the evening sun shining dimly through a hole in the ceiling far above.")
input("You can see a tunnel leading north, a tunnel leading south, a small tunnel leading east, and a small lake to the west.")
input("Far above you in the ceiling, you can dimly see a tattered rope hanging down from the hole in the ceiling.")