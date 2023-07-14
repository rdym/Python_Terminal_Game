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

class Map():
    def __init__(self, player_x = 9, player_y = 10):
        self.player_x = player_x
        self.player_y = player_y
        self.map = [['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'R', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'L', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'M', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.blank_map = [['?'] * self.width for _ in range(self.height)]
        self.have_map = True
        self.can_move_north = False
        self.can_move_south = False
        self.can_move_east = False
        self.can_move_west = False
        

    def __repr__(self):
        return "Map(height = {height}, width = {width}, player_x = {player_x}, player_y = {player_y})".format(height = self.height, width = self.width, player_x = self.player_x, player_y = self.player_y)
    
    def reveal_map(self, x, y):
        for i, row in enumerate(self.blank_map):

            y_above = i - 1
            if y_above < 0:
                        y_above = 0

            y_below = i + 1
            if y_below > self.height - 1:
                y_below = self.height - 1

            for j, char in enumerate(row):

                x_left = j - 1
                if x_left < 0:
                    x_left = 0

                x_right = j + 1
                if x_right > self.width - 1:
                    x_right = self.width - 1

                if i == y and j == x:
                    
                    self.blank_map[i][j] = self.map[i][j]
                    self.blank_map[y_above][j] = self.map[y_above][j]
                    self.blank_map[y_below][j] = self.map[y_below][j]
                    self.blank_map[i][x_left] = self.map[i][x_left]
                    self.blank_map[i][x_right] = self.map[i][x_right]
                    self.blank_map[y_above][x_left] = self.map[y_above][x_left]
                    self.blank_map[y_above][x_right] = self.map[y_above][x_right]
                    self.blank_map[y_below][x_left] = self.map[y_below][x_left]
                    self.blank_map[y_below][x_right] = self.map[y_below][x_right]
        return self.blank_map
    
    def can_move(self, x, y):
        can_move_directions = []
        if self.map[y-1][x] == ' ':
            self.can_move_north = True
            can_move_directions.append('north')
        if self.map[y-1][x] == 'R':
            self.can_move_north = True
            can_move_directions.append('north to pickup a rope')
        if self.map[y + 1][x] == ' ':
            self.can_move_south = True
            can_move_directions.append('south')
        if self.map[y + 1][x] == 'R':
            self.can_move_south = True
            can_move_directions.append('south to pickup a rope')
        if self.map[y][x + 1] == ' ':
            self.can_move_east = True
            can_move_directions.append('east')
        if self.map[y][x + 1] == 'R':
            self.can_move_east = True
            can_move_directions.append('east to pickup a rope')
        if self.map[y][x - 1] == ' ':
            self.can_move_west = True
            can_move_directions.append('west')
        if self.map[y][x - 1] == 'R':
            self.can_move_west = True
            can_move_directions.append('west to pickup a rope')
        new_can_move = can_move_directions[0]
        if len(can_move_directions) > 1:
            if len(can_move_directions) == 2:
                new_can_move += ' or ' + can_move_directions[1]
            elif len(can_move_directions) == 3:
                new_can_move += ', ' + can_move_directions[1] + ' or ' + can_move_directions[2]
            else:
                print("Something went wrong")
        print("You can't go that way! It looks like you can go " + new_can_move + " though!")

    
    def move(self, direction):
        if direction.lower() == 'north':
            new_cell = self.map[self.player_y - 1][self.player_x]
            if new_cell == ' ':
                self.player_y -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'M':
                print("You found a map!")
                self.have_map = True
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
        elif direction.lower() == 'south':
            new_cell = self.map[self.player_y + 1][self.player_x]
            if new_cell == ' ':
                self.player_y += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'M':
                print("You found a map!")
                self.have_map = True
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
        elif direction.lower() == 'east':
            new_cell = self.map[self.player_y][self.player_x + 1]
            if new_cell == ' ':
                self.player_x += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'M':
                print("You found a map!")
                self.have_map = True
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
        elif direction.lower() == 'west':
            new_cell = self.map[self.player_y][self.player_x - 1]
            if new_cell == ' ':
                self.player_x -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'M':
                print("You found a map!")
                self.have_map = True
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)

    def print_map(self):
        map_string = ""
        for row in self.map:
            for char in row:
                map_string += char
            map_string += "\n"
        print(map_string)

    def print_map_with_player(self):
        if self.have_map == True:
            map_string = ""
            for i, row in enumerate(self.blank_map):
                for j, char in enumerate(row):
                    if i == self.player_y and char == ' ' and j == self.player_x:
                        map_string += 'P'
                    else:
                        map_string += char
                map_string += "\n"
            print(map_string)
        else:
            print("You haven't found a map yet. You can't see where you are on the map.")

class Player:
    def __init__(self, name = ""):
        self.name = name
        self.inventory = ['lantern']
        self.location = "cavern"
        self.is_alive = True
        self.health = 10
        self.max_health = 10
        self.is_lantern_lit = False
        self.have_rope = False
        self.have_map = False

    def __repr__(self):
        return "{name} is currently in the {location}.".format(name = self.name, location = self.location)

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

    # def inventory(self):
    #     if len(self.inventory) == 0:
    #         print_line("You are not carrying anything.\n")
    #     else:
    #         print_line("You are carrying:")
    #         for item in self.inventory:
    #             print_line(item)

    def take(self, item):
        if item == "lantern":
            if self.location == "cavern":
                if "lantern" in self.inventory:
                    print_line("You already have a lantern.")
                else:
                    self.inventory.append("lantern")
                    print_line("You take the lantern.")
            else:
                print_line("You can't take that.")
        else:
            print_line("You can't take that.")

    def drop(self, item):
        if item == "lantern":
            if self.location == "cavern":
                if "lantern" in self.inventory:
                    self.inventory.remove("lantern")
                    print_line("You drop the lantern.")
                else:
                    print_line("You don't have a lantern.")
            else:
                print_line("You can't drop that.")
        else:
            print_line("You can't drop that.")

    def use(self, item):
        # if item == "lantern":
        #     if self.location == "cavern":
        #         if "lantern" in self.inventory:
        #             if self.is_lantern_lit == True:
        #                 print_line("The lantern is already lit.")
        #             else:
        #                 self.is_lantern_lit = True
        #                 print_line("You light the lantern.")
        #         else:
        #             print_line("You don't have a lantern.")
        #     else:
        #         print_line("You can't use that.")
        if item == "rope":
            if self.location == "rope":
                if self.have_rope == True:
                    print_line("You are already holding the rope.")
                else:
                    self.have_rope = True
                    print_line("You grab the rope.")
            else:
                print_line("You can't use that.")
        # if item == "map":

        else:
            print_line("You can't use that.")

    def help(self):
        print_line("You can move around the cave by typing 'go' and then the direction you want to go in. For example, 'go north' or 'go south'.\n")
        print_line("You can look around the room you are in by typing 'look'.\n")
        print_line("You can pick up items by typing 'take' and then the name of the item. For example, 'take lantern'.\n")
        print_line("You can drop items by typing 'drop' and then the name of the item. For example, 'drop lantern'.\n")
        print_line("You can use items by typing 'use' and then the name of the item. For example, 'use lantern'.\n")
        print_line("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.\n")
        print_line("You can type 'quit' to quit the game at any time.\n")

    def quit(self):
        print_line("You quit the game.")
        exit()

player = Player()
map1 = Map()

# ascii_banner = pyfiglet.figlet_format("The Cave")
# print(ascii_banner)
# print_line_input("Welcome to The Cave! You have fallen into a cave in a remote location and must find your way out. You have a limited amount of time to escape before you run out of supplies. Good luck!")
# print_line_input("You will be able to move around the cave by typing 'go' and then the direction you want to go in. For example, 'go north' or 'go south'.")
# input("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
# input("You can pick up items by typing 'take' and then the name of the item. For example, 'take lantern'.")
# input("You can drop items by typing 'drop' and then the name of the item. For example, 'drop lantern'.")
# input("You can use items by typing 'use' and then the name of the item. For example, 'use lantern'.")
# input("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.")
# input("You can type 'quit' to quit the game at any time.")
# print_line_input("Press enter to begin.")
# input()
os.system('cls')

opening_banner = pyfiglet.figlet_format("Welcome to the Cave!")
print(opening_banner)
sleep(0.5)

# print_line_input("You wake up in a dim cave. You can't remember how you got here or where you are. You can't see anything, but you can feel something in your pocket.")
# print_line_input("You take the item out of your pocket and feel it. It's a lantern! You can use this to see in the dark. You light the lantern and look around.")
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
    if action == "north" or action == "south" or action == "east" or action == "west":
        map1.move(action)
        map1.print_map_with_player()
    elif action == "look":
        player.look()
    # elif action == "inventory":
    #     player.inventory()
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
    elif action == "map":
        map1.print_map_with_player()
    elif action == "quit":
        player.quit()
    elif action == "print1":
        print("This is working")
    else:
        print_line("I don't understand that command. Please try again.\n")