import pyfiglet
import os
from time import sleep
import sys

def print_line_input(line):
    for char in line:
        print(char, end='', flush=True)
        sleep(0.02)
    input()

def print_line(line):
    for char in line:
        print(char, end='', flush=True)
        sleep(0.02)

class Player:

    def __init__(self, name = "nameless player"):
        self.name = name
        self.inventory = []
        self.location = "cavern"
        self.is_alive = True
        self.health = 10
        self.max_health = 10
        self.is_torch_lit = False

    def __repr__(self):
        return "{name} is currently in the {location}.".format(name = self.name, location = self.location)
    
    def go(self, direction):
        if direction == "north":
            if self.location == "cavern":
                self.location = "tunnel"
                print_line("You move north into the tunnel.")
            elif self.location == "tunnel":
                self.location = "cavern"
                print_line("You move north into the cavern.")
            elif self.location == "lake":
                print_line("You can't go north from here.")
            elif self.location == "rope":
                print_line("You can't go north from here.")
        elif direction == "south":
            if self.location == "cavern":
                print_line("You can't go south from here.")
            elif self.location == "tunnel":
                print_line("You can't go south from here.")
            elif self.location == "lake":
                print_line("You can't go south from here.")
            elif self.location == "rope":
                self.location = "cavern"
                print_line("You move south into the cavern.")
        elif direction == "east":
            if self.location == "cavern":
                print_line("You can't go east from here.")
            elif self.location == "tunnel":
                print_line("You can't go east from here.")
            elif self.location == "lake":
                self.location = "cavern"
                print_line("You move east into the cavern.")
            elif self.location == "rope":
                print_line("You can't go east from here.")
        elif direction == "west":
            if self.location == "cavern":
                print_line("You can't go west from here.")
            elif self.location == "tunnel":
                print_line("You can't go west from here.")
            elif self.location == "lake":
                print_line("You can't go west from here.")
            elif self.location == "rope":
                self.location = "cavern"
                print_line("You move west into the cavern.")
        else:
            print_line("You can't go that way.")

    def look(self):
        if self.location == "cavern":
            print_line("You are lying in the centre of a large cavern, with the evening sun shining dimly through a hole in the ceiling far above.\n")
            print_line("You can see a tunnel leading north, a small tunnel leading south, a small tunnel leading east, and a small lake to the west.\n")
            print_line("Far above you in the ceiling, you can dimly see a tattered rope hanging down from the hole in the ceiling.\n")
        elif self.location == "tunnel":
            print_line("You are in a small tunnel. There is a large cavern to the south.\n")
        elif self.location == "lake":
            print_line("You are standing on the shore of a small lake. There is a large cavern to the east.\n")
        elif self.location == "rope":
            print_line("You are hanging from a rope. There is a large cavern below you.\n")

    def inventory(self):
        if len(self.inventory) == 0:
            print_line("You are not carrying anything.\n")
        else:
            print_line("You are carrying:")
            for item in self.inventory:
                print_line(item)

    def take(self, item):
        if item == "torch":
            if self.location == "cavern":
                if "torch" in self.inventory:
                    print_line("You already have a torch.")
                else:
                    self.inventory.append("torch")
                    print_line("You take the torch.")
            else:
                print_line("You can't take that.")
        else:
            print_line("You can't take that.")

    def drop(self, item):
        if item == "torch":
            if self.location == "cavern":
                if "torch" in self.inventory:
                    self.inventory.remove("torch")
                    print_line("You drop the torch.")
                else:
                    print_line("You don't have a torch.")
            else:
                print_line("You can't drop that.")
        else:
            print_line("You can't drop that.")

    def use(self, item):
        if item == "torch":
            if self.location == "cavern":
                if "torch" in self.inventory:
                    if self.is_torch_lit == True:
                        print_line("The torch is already lit.")
                    else:
                        self.is_torch_lit = True
                        print_line("You light the torch.")
                else:
                    print_line("You don't have a torch.")
            else:
                print_line("You can't use that.")
        else:
            print_line("You can't use that.")

    def help(self):
        print_line("You can move around the cave by typing 'go' and then the direction you want to go in. For example, 'go north' or 'go south'.\n")
        print_line("You can look around the room you are in by typing 'look'.\n")
        print_line("You can pick up items by typing 'take' and then the name of the item. For example, 'take torch'.\n")
        print_line("You can drop items by typing 'drop' and then the name of the item. For example, 'drop torch'.\n")
        print_line("You can use items by typing 'use' and then the name of the item. For example, 'use torch'.\n")
        print_line("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.\n")
        print_line("You can type 'quit' to quit the game at any time.\n")
        print_line("You can type 'save' to save the game at any time.\n")
        print_line("You can type 'load' to load the game at any time.\n")
        print_line("You can type 'restart' to restart the game at any time.\n")
        print_line("You can type 'reset' to reset the game at any time.\n")

    def quit(self):
        print_line("You quit the game.")
        exit()

    # def save(self):
    #     print_line("You save the game.")
    #     exit()

    # def load(self):
    #     print_line("You load the game.")
    #     exit()

    # def restart(self):
    #     print_line("You restart the game.")
    #     exit()

    # def reset(self):
    #     print_line("You reset the game.")
    #     exit()

player = Player()

# ascii_banner = pyfiglet.figlet_format("The Cave")
# print(ascii_banner)
# print_line_input("Welcome to The Cave! You have fallen into a cave in a remote location and must find your way out. You have a limited amount of time to escape before you run out of supplies. Good luck!")
# print_line_input("You will be able to move around the cave by typing 'go' and then the direction you want to go in. For example, 'go north' or 'go south'.")
# input("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
# input("You can pick up items by typing 'take' and then the name of the item. For example, 'take torch'.")
# input("You can drop items by typing 'drop' and then the name of the item. For example, 'drop torch'.")
# input("You can use items by typing 'use' and then the name of the item. For example, 'use torch'.")
# input("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.")
# input("You can type 'quit' to quit the game at any time.")
# input("You can type 'save' to save the game at any time.")
# input("You can type 'load' to load the game at any time.")
# input("You can type 'restart' to restart the game at any time.")
# input("You can type 'reset' to reset the game at any time.")
# print_line_input("Press enter to begin.")
# input()
os.system('cls')

opening_banner = pyfiglet.figlet_format("Welcome to the Cave!")
print(opening_banner)
sleep(0.5)

# print_line_input("You wake up in a dim cave. You can't remember how you got here or where you are. You can't see anything, but you can feel something in your pocket.")
# print_line_input("You take the item out of your pocket and feel it. It's a torch! You can use this to see in the dark. You light the torch and look around.")
# print_line_input("You are lying in the centre of a large cavern, with the evening sun shining dimly through a hole in the ceiling far above.")
# print_line_input("You can see a tunnel leading north, a tunnel leading south, a small tunnel leading east, and a small lake to the west.")
# print_line_input("Far above you in the ceiling, you can dimly see a tattered rope hanging down from the hole in the ceiling.")
# print_line_input("Suddenly, you hear static coming from your pocket. You take out the radio and hear a voice.")
# print_line_input("'KRRRRSSSSSHZZZZZTTHZZZZZ...Hello? Is anyone there?...KRRRRSSSSSHZZZZZTTHZZZZZ...He...KRRRRSSSSSHZZZZZTTHZZZZZ...Hello...yone the...KRRRSSHHT'")
# print_line_input("You pick up the radio and say 'Hello'.")
# print_line_input("'KRRRRSSH Hello! Wow someone can hear me! I'm so glad! I heard a loud noise and thought someone must be down there!'")

print_line("'What's your name?'\n")
player.name = input("Please enter your name: ")
print_line_input("'Wow I can't believe I found you {name}! I'm so glad you're okay! I think I can see you moving below'. You see a figure waving at you far above.".format(name = player.name))
print_line_input("'I'm going to try and find a way to get you out of there. I'll be back soon!'")

while player.is_alive == True:
    print_line("What do you want to do?\n")
    action = input("Please enter a command: ")
    if action == "go":
        direction = input("Please enter a direction: ")
        player.go(direction)
    elif action == "look":
        player.look()
    elif action == "inventory":
        player.inventory()
    elif action == "take":
        item = input("Please enter an item: ")
        player.take(item)
    elif action == "drop":
        item = input("Please enter an item: ")
        player.drop(item)
    elif action == "use":
        item = input("Please enter an item: ")
        player.use(item)
    elif action == "help":
        player.help()
    elif action == "quit":
        player.quit()
    # elif action == "save":
    #     player.save()
    # elif action == "load":
    #     player.load()
    # elif action == "restart":
    #     player.restart()
    # elif action == "reset":
    #     player.reset()
    else:
        print_line("I don't understand that command. Please try again.\n")