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


map1 = Map()

class Player:
    def __init__(self, name = ""):
        self.name = name
        self.inventory = []
        self.is_alive = True
        self.health = 10
        self.max_health = 10
        self.is_lantern_lit = False
        self.have_rope = False
        self.have_map = False
        self.player_x = map1.player_x
        self.player_y = map1.player_y

    def __repr__(self):
        return "The current player is called {name}.".format(name = self.name, location = self.location)

    def look(self):

        look_directions = []
        x = map1.player_x
        y = map1.player_y

        if map1.map[y-1][x] == ' ':
            look_directions.append('the path is clear to the north')
        elif map1.map[y-1][x] == 'R':
            look_directions.append('there is a rope to the north')
        elif map1.map[y-1][x] == 'M':
            look_directions.append('there is a map to the north')
        elif map1.map[y-1][x] == 'L':
            look_directions.append('there is a ladder to the north')
        else:
            look_directions.append('there is a wall to the north')

        if map1.map[y + 1][x] == ' ':
            look_directions.append('the path is clear to the south')
        elif map1.map[y + 1][x] == 'R':
            look_directions.append('there is a rope to the south')
        elif map1.map[y + 1][x] == 'M':
            look_directions.append('there is a map to the south')
        elif map1.map[y + 1][x] == 'L':
            look_directions.append('there is a ladder to the south')
        else:
            look_directions.append('there is a wall to the south')

        if map1.map[y][x + 1] == ' ':
            look_directions.append('the path is clear to the east')
        elif map1.map[y][x + 1] == 'R':
            look_directions.append('there is a rope to the east')
        elif map1.map[y][x + 1] == 'M':
            look_directions.append('there is a map to the east')
        elif map1.map[y][x + 1] == 'L':
            look_directions.append('there is a ladder to the east')
        else:
            look_directions.append('there is a wall to the east')

        if map1.map[y][x - 1] == ' ':
            look_directions.append('the path is clear to the west')
        elif map1.map[y][x - 1] == 'R':
            look_directions.append('there is a rope to the west')
        elif map1.map[y][x - 1] == 'M':
            look_directions.append('there is a map to the west')
        elif map1.map[y][x - 1] == 'L':
            look_directions.append('there is a ladder to the west')
        else:
            look_directions.append('there is a wall to the west')

        print_line("You look around and see that " + look_directions[0] + ", " + look_directions[1] + ", " + look_directions[2] + " and " + look_directions[3] + "." + "\n")

    def check_inventory(self):
        if len(self.inventory) == 0:
            print_line("You are not carrying anything.\n")
        else:
            print_line("You are carrying:")
            for item in self.inventory:
                print_line(item)

    # def take(self, item):
    #     if item == "lantern":
    #         if self.location == "cavern":
    #             if "lantern" in self.inventory:
    #                 print_line("You already have a lantern.")
    #             else:
    #                 self.inventory.append("lantern")
    #                 print_line("You take the lantern.")
    #         else:
    #             print_line("You can't take that.")
    #     else:
    #         print_line("You can't take that.")

    # def drop(self, item):
    #     if item == "lantern":
    #         if self.location == "cavern":
    #             if "lantern" in self.inventory:
    #                 self.inventory.remove("lantern")
    #                 print_line("You drop the lantern.")
    #             else:
    #                 print_line("You don't have a lantern.")
    #         else:
    #             print_line("You can't drop that.")
    #     else:
    #         print_line("You can't drop that.")

    def use(self, item, target = None):

        if item == "rope":
            if self.have_rope == True:
                if target == "ladder":
                    print_line("You can't use the rope on the ladder.\n")
                elif target == "ledge":
                    print_line("You tie the rope to the ledge and climb down to the bottom.\n")
                    # Need to add some functionality here to move the player to the bottom of the cave
                    # Will likely need to add a second map layer, a variable that controls which layer is displayed and a function to switch between the two
                else:
                    print_line("You can't use the rope on that.\n")
            else:
                print_line("You don't have a rope.\n")
        elif item == "map":
            if self.have_map == True:
                map1.print_map_with_player()
            else:
                print_line("You don't have a map.\n")

        # if item == "map":

        else:
            print_line("You don't have that item.\n")

    def help(self):
        print_line("You will be able to move around the cave by typing the direction you want to go in. For example, 'north' or 'south'.\n")
        print_line("You can look around yourself by typing 'look'.\n")
        # print_line("You can pick up items by typing 'take' and then the name of the item. For example, 'take lantern'.\n")
        # print_line("You can drop items by typing 'drop' and then the name of the item. For example, 'drop lantern'.\n")
        print_line("You can use items by typing 'use' and then the name of the 'item' and the 'target' for the item's use.\n")
        # print_line("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.\n") # Is this unnecessary?
        print_line("You can type 'quit' to quit the game at any time.\n")

    def quit(self):
        print_line("You quit the game.")
        exit()

player = Player()

# ascii_banner = pyfiglet.figlet_format("The Cave")
# print(ascii_banner)
# print_line_input("Welcome to The Cave! You have fallen into a cave in a remote location and must find your way out. You have a limited amount of time to escape before you run out of supplies. Good luck!")
# print_line_input("You will be able to move around the cave by typing the direction you want to go in. For example, 'north' or 'south'.")
# print_line_input("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
# print_line_input("You can pick up items by typing 'take' and then the name of the item. For example, 'take lantern'.")
# print_line_input("You can drop items by typing 'drop' and then the name of the item. For example, 'drop lantern'.")
# print_line_input("You can use items by typing 'use' and then the name of the item. For example, 'use lantern'.")
# print_line_input("You can also type 'help' to see this list of commands again...if anyone is close enough to help you.")
# print_line_input("You can type 'quit' to quit the game at any time.")
# print_line_input("Press enter to begin.")
os.system('cls')

opening_banner = pyfiglet.figlet_format("Welcome to the Cave!")
print(opening_banner)
sleep(0.5)

# print_line_input("You wake up in a dark cave. You can't remember how you got here or where you are. You can't see anything, but you can feel something next to you on the ground.")
# print_line_input("You take the item out of your pocket and feel it. It's a lantern! You can use this to see in the dark. You light the lantern and look around.")
# print_line_input("You can see a short distance around yourself from the dim lantern light. You are lying in the centre of a large cavern, with the evening sun shining dimly through a hole in the ceiling far above.")
# print_line_input("You can dimly make out a tattered rope hanging down from the hole in the ceiling.")
# print_line_input("Suddenly, you hear static coming from your pocket. You take out the radio and hear a voice.")
# print_line_input("'KRRRRSSSSSHZZZZZTTHZZZZZ...Hello? Is anyone there?...KRRRRSSSSSHZZZZZTTHZZZZZ...He...KRRRRSSSSSHZZZZZTTHZZZZZ...Hello...yone the...KRRRSSHHT'")
# print_line_input("You pick up the radio and say 'Hello'.")
# print_line_input("'KRRRRSSH Hello! Wow someone can hear me! I'm so glad! I heard a loud noise and thought someone must be down there!'")
# print_line("'What's your name?'\n")
# player.name = input("Please enter your name: ")
# print_line_input("'Wow I can't believe I found you {name}! I'm so glad you're okay! I think I can see you moving below'. You see a figure waving at you far above.".format(name = player.name))
# print_line_input("'I'm going to try and find a way to get you out of there. I'll be back soon!'")

while player.is_alive == True:
    print_line("What do you want to do?\n")
    action = input("Please enter a command: ")
    if action == "north" or action == "south" or action == "east" or action == "west":
        map1.move(action)
    elif action == "look":
        player.look()
    elif action == "inventory":
        player.check_inventory()
    # elif action == "take": # Consider removing this command
    #     item = input("Please enter an item: ")
    #     player.take(item)
    # elif action == "drop": # Consider removing this command
    #     item = input("Please enter an item: ")
    #     player.drop(item)
    elif action == "use":
        item, *target = input("Please enter an item and target (if required): ").split()
        if item == "map":
            player.use(item)
        else:
            if len(target) == 0 and item in player.inventory: # Check whether this is the correct syntax
                print_line("You need to specify a target for that item.\n")
            else:
                player.use(item, target[0])
    elif action == "help":
        player.help()
    # elif action == "map": # Consider moving this functionality to the use command
    #     map1.print_map_with_player()
    elif action == "quit":
        player.quit()
    elif action == "print1":
        print("This is working")
    else:
        print_line("I don't understand that command. Please try again.\n")