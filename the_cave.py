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
    def __init__(self, player_x = 15, player_y = 12):
        self.player_x = player_x
        self.player_y = player_y
        self.start_map = [['C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','U',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C',' ',' ',' ','D','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','D','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C',' ',' ','B',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C',' ','C','C','C','C','C',' ',' ',' ',' ','C'],
                          ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C',' ','C','C','C','C','C',' ',' ',' ','R','C'],
                          ['C','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C',' ','C','C','C','C',' ',' ',' ',' ',' ','C'],
                          ['C','C','C','C',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','C'],
                          ['C','C','C','C',' ','M','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C'],
                          ['C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C']]
        
        self.down_1_map = [['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ','C','C','C','C','C'],
                            ['C','C','C','C','C',' ',' ',' ','C','C','C',' ','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C'],
                            ['C','C','C','C',' ',' ','C','C','C','C','C',' ','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C'],
                            ['C','C',' ',' ',' ','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C',' ','C','C','C',' ',' ',' ','C','C','C'],
                            ['C','C',' ','C','C','C','C','C','C','C','U',' ',' ','C','C','C','C','C','C','C',' ','C','C','C',' ',' ',' ','C','C','C'],
                            ['C','C',' ','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','U','C','C','C','C',' ',' ','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ','C','C'],
                            ['C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C',' ',' ','C','C'],
                            ['C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C'],
                            ['C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C'],
                            ['C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C',' ','C','C','C'],
                            ['C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C'],
                            ['C','C','C','C','C',' ','C','C','C','C','C','C',' ',' ','C',' ',' ','C','C','C','C','C','C','C','C',' ',' ','C','C','C'],
                            ['C','C','C','C','C',' ','C','C','C','C','C',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C','C'],
                            ['C','G',' ',' ',' ',' ','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C',' ',' ','C','C','C','C','C','C'],
                            ['C',' ',' ','C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C']]
        
        self.up_1_map = [['C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','D',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','E',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C',' ',' ',' ','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C',' ',' ',' ','E','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ','C','C',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ','C','C',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C']]
        
        self.map = self.start_map
        self.current_level = 0
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.blank_map = [['?'] * self.width for _ in range(self.height)]
        self.have_map = False
        self.have_grapple = False
        self.have_rope = False
        self.have_pickaxe = False     

    def __repr__(self):
        return "Map(height = {height}, width = {width}, player_x = {player_x}, player_y = {player_y})".format(height = self.height, width = self.width, player_x = self.player_x, player_y = self.player_y)
    
    def game_won(self):
        print("You found the exit! You win!")
        exit()
    
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
            can_move_directions.append('north')
        elif self.map[y-1][x] == 'R':
            can_move_directions.append('north to pickup a rope')
        elif self.map[y-1][x] == 'M':
            can_move_directions.append('north to pickup a map')
        elif self.map[y-1][x] == 'E':
            can_move_directions.append('north to go to the exit')
        elif self.map[y-1][x] == 'G':
            can_move_directions.append('north to pick up a grappling hook')
        elif self.map[y-1][x] == 'B':
            can_move_directions.append('north is blocked by rubble')
        elif self.map[y-1][x] == 'A':
            can_move_directions.append('north to pick up a pickaxe')
        elif self.map[y-1][x] == 'U':
            can_move_directions.append('north to a ledge above')
        elif self.map[y-1][x] == 'D':
            can_move_directions.append('north to a ledge below')

        if self.map[y + 1][x] == ' ':
            can_move_directions.append('south')
        elif self.map[y + 1][x] == 'R':
            can_move_directions.append('south to pickup a rope')
        elif self.map[y + 1][x] == 'M':
            can_move_directions.append('south to pickup a map')
        elif self.map[y + 1][x] == 'E':
            can_move_directions.append('south to go to the exit')
        elif self.map[y + 1][x] == 'G':
            can_move_directions.append('south to pick up a grappling hook')
        elif self.map[y + 1][x] == 'B':
            can_move_directions.append('south is blocked by rubble')
        elif self.map[y + 1][x] == 'A':
            can_move_directions.append('south to pick up a pickaxe')
        elif self.map[y + 1][x] == 'U':
            can_move_directions.append('south to a ledge above')
        elif self.map[y + 1][x] == 'D':
            can_move_directions.append('south to a ledge below')
            
        if self.map[y][x + 1] == ' ':
            can_move_directions.append('east')
        elif self.map[y][x + 1] == 'R':
            can_move_directions.append('east to pickup a rope')
        elif self.map[y][x + 1] == 'M':
            can_move_directions.append('east to pickup a map')
        elif self.map[y][x + 1] == 'E':
            can_move_directions.append('east to go to the exit')
        elif self.map[y][x + 1] == 'G':
            can_move_directions.append('east to pick up a grappling hook')
        elif self.map[y][x + 1] == 'B':
            can_move_directions.append('east is blocked by rubble')
        elif self.map[y][x + 1] == 'A':
            can_move_directions.append('east to pick up a pickaxe')
        elif self.map[y][x + 1] == 'U':
            can_move_directions.append('east to a ledge above')
        elif self.map[y][x + 1] == 'D':
            can_move_directions.append('east to a ledge below')
            
        if self.map[y][x - 1] == ' ':
            can_move_directions.append('west')
        elif self.map[y][x - 1] == 'R':
            can_move_directions.append('west to pickup a rope')
        elif self.map[y][x - 1] == 'M':
            can_move_directions.append('west to pickup a map')
        elif self.map[y][x - 1] == 'E':
            can_move_directions.append('west to go to the exit')
        elif self.map[y][x - 1] == 'G':
            can_move_directions.append('west to pick up a grappling hook')
        elif self.map[y][x - 1] == 'B':
            can_move_directions.append('west is blocked by rubble')
        elif self.map[y][x - 1] == 'A':
            can_move_directions.append('west to pick up a pickaxe')
        elif self.map[y][x - 1] == 'U':
            can_move_directions.append('west to a ledge above')
        elif self.map[y][x - 1] == 'D':
            can_move_directions.append('west to a ledge below')
            
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
        
        if direction.lower() == 'north' or direction.lower() == 'n':
            new_cell = self.map[self.player_y - 1][self.player_x]
            if new_cell == ' ':
                self.player_y -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.have_rope = True
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'M':
                print("You found a map!")
                self.have_map = True
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'E':
                print("You found the exit!")
                self.player_y -= 1
                self.reveal_map(self.player_x, self.player_y)
                self.game_won()
            elif new_cell == 'G':
                print("You found a grappling hook!")
                self.have_grapple = True
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
            elif new_cell == 'A':
                print("You found a pickaxe!")
                self.have_pickaxe = True
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'U':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb up the ledge.")
                    self.player_y -= 1
                    self.current_level += 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb up there, it's too high! You'll need something to help you climb up.")
                    self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'D':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb down the ledge.")
                    self.player_y -= 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                elif self.have_rope == True:
                    print("You use your rope to climb down the ledge.")
                    self.player_y -= 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb down there, it's too high! You'll need something to help you climb down.")
                    self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
                
        elif direction.lower() == 'south' or direction.lower() == 's':
            new_cell = self.map[self.player_y + 1][self.player_x]
            if new_cell == ' ':
                self.player_y += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_rope = True
            elif new_cell == 'M':
                print("You found a map!")
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_map = True
            elif new_cell == 'E':
                print("You found the exit!")
                self.player_y += 1
                self.reveal_map(self.player_x, self.player_y)
                self.game_won()
            elif new_cell == 'G':
                print("You found a grappling hook!")
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_grapple = True
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
            elif new_cell == 'A':
                print("You found a pickaxe!")
                self.player_y += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_pickaxe = True
            elif new_cell == 'U':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb up the ledge.")
                    self.player_y += 1
                    self.current_level += 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb up there, it's too high! You'll need something to help you climb up.")
                    self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'D':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb down the ledge.")
                    self.player_y += 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                elif self.have_rope == True:
                    print("You use your rope to climb down the ledge.")
                    self.player_y += 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb down there, it's too high! You'll need something to help you climb down.")
                    self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
                
        elif direction.lower() == 'east' or direction.lower() == 'e':
            new_cell = self.map[self.player_y][self.player_x + 1]
            if new_cell == ' ':
                self.player_x += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_rope = True
            elif new_cell == 'M':
                print("You found a map!")
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_map = True
            elif new_cell == 'E':
                print("You found the exit!")
                self.player_x += 1
                self.reveal_map(self.player_x, self.player_y)
                self.game_won()
            elif new_cell == 'G':
                print("You found a grappling hook!")
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_grapple = True
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
            elif new_cell == 'A':
                print("You found a pickaxe!")
                self.player_x += 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_pickaxe = True
            elif new_cell == 'U':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb up the ledge.")
                    self.player_x += 1
                    self.current_level += 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb up there, it's too high! You'll need something to help you climb up.")
                    self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'D':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb down the ledge.")
                    self.player_x += 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                elif self.have_rope == True:
                    print("You use your rope to climb down the ledge.")
                    self.player_x += 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb down there, it's too high! You'll need something to help you climb down.")
                    self.reveal_map(self.player_x, self.player_y)
            else:
                self.can_move(self.player_x, self.player_y)
                
        elif direction.lower() == 'west' or direction.lower() == 'w':
            new_cell = self.map[self.player_y][self.player_x - 1]
            if new_cell == ' ':
                self.player_x -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_rope = True
            elif new_cell == 'M':
                print("You found a map!")
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_map = True
            elif new_cell == 'E':
                print("You found the exit!")
                self.player_x -= 1
                self.reveal_map(self.player_x, self.player_y)
                self.game_won()
            elif new_cell == 'G':
                print("You found a grappling hook!")
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_grapple = True
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
            elif new_cell == 'A':
                print("You found a pickaxe!")
                self.player_x -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
                self.have_pickaxe = True
            elif new_cell == 'U':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb up the ledge.")
                    self.player_x -= 1
                    self.current_level += 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb up there, it's too high! You'll need something to help you climb up.")
                    self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'D':
                if self.have_grapple == True:
                    print("You use your grappling hook to climb down the ledge.")
                    self.player_x -= 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                elif self.have_rope == True:
                    print("You use your rope to climb down the ledge.")
                    self.player_x -= 1
                    self.current_level -= 1
                    self.reveal_map(self.player_x, self.player_y)
                else:
                    print("You can't climb down there, it's too high! You'll need something to help you climb down.")
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
            
    def print_area_around_player(self):
        map_string = ""
        player_map = [self.map[self.player_y - 1][self.player_x - 1:self.player_x + 2],
                      self.map[self.player_y][self.player_x - 1:self.player_x + 2],
                      self.map[self.player_y + 1][self.player_x - 1:self.player_x + 2]]
        for i, row in enumerate(player_map):
            for j, char in enumerate(row):
                if i == 1 and j == 1:
                    map_string += 'P'
                else:
                    map_string += char
            map_string += "\n"
        print(map_string)
    
    def change_level(self):
        if self.current_level == 0:
            self.map = self.start_map
        elif self.current_level == 1:
            self.map = self.up_1_map
        elif self.current_level == -1:
            self.map = self.down_1_map
        else:
            print("Something went wrong with the map levels")

map1 = Map()

class Player:
    def __init__(self, name = ""):
        self.name = name
        self.inventory = []
        self.is_alive = True
        self.health = 10
        self.max_health = 10
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
        elif map1.map[y-1][x] == 'B':
            look_directions.append('there is a pile of rubble to the north')
        elif map1.map[y-1][x] == 'A':
            look_directions.append('there is a pickaxe to the north')
        elif map1.map[y-1][x] == 'U':
            look_directions.append('there is a ledge above to the north')
        elif map1.map[y-1][x] == 'D':
            look_directions.append('there is a ledge below to the north')
        elif map1.map[y-1][x] == 'E':
            look_directions.append('there is the exit to the north')
        elif map1.map[y-1][x] == 'G':
            look_directions.append('there is a grappling hook to the north')
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
        elif map1.map[y + 1][x] == 'B':
            look_directions.append('there is a pile of rubble to the south')
        elif map1.map[y + 1][x] == 'A':
            look_directions.append('there is a pickaxe to the south')
        elif map1.map[y + 1][x] == 'U':
            look_directions.append('there is a ledge above to the south')
        elif map1.map[y + 1][x] == 'D':
            look_directions.append('there is a ledge below to the south')
        elif map1.map[y + 1][x] == 'E':
            look_directions.append('there is the exit to the south')
        elif map1.map[y + 1][x] == 'G':
            look_directions.append('there is a grappling hook to the south')
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
        elif map1.map[y][x + 1] == 'B':
            look_directions.append('there is a pile of rubble to the east')
        elif map1.map[y][x + 1] == 'A':
            look_directions.append('there is a pickaxe to the east')
        elif map1.map[y][x + 1] == 'U':
            look_directions.append('there is a ledge above to the east')
        elif map1.map[y][x + 1] == 'D':
            look_directions.append('there is a ledge below to the east')
        elif map1.map[y][x + 1] == 'E':
            look_directions.append('there is the exit to the east')
        elif map1.map[y][x + 1] == 'G':
            look_directions.append('there is a grappling hook to the east')
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
        elif map1.map[y][x - 1] == 'B':
            look_directions.append('there is a pile of rubble to the west')
        elif map1.map[y][x - 1] == 'A':
            look_directions.append('there is a pickaxe to the west')
        elif map1.map[y][x - 1] == 'U':
            look_directions.append('there is a ledge above to the west')
        elif map1.map[y][x - 1] == 'D':
            look_directions.append('there is a ledge below to the west')
        elif map1.map[y][x - 1] == 'E':
            look_directions.append('there is the exit to the west')
        elif map1.map[y][x - 1] == 'G':
            look_directions.append('there is a grappling hook to the west')
        else:
            look_directions.append('there is a wall to the west')

        print_line("You look around and see that " + look_directions[0] + ", " + look_directions[1] + ", " + look_directions[2] + " and " + look_directions[3] + "." + "\n")

    def check_inventory(self):
        inventory_string = ""
        if len(self.inventory) > 1:
            if len(self.inventory) == 2:
                inventory_string += "a " + self.inventory[0] + " and a " + self.inventory[1]
            elif len(self.inventory) > 2:
                for item in self.inventory[:-1]:
                    inventory_string += "a " + item + ", "
                inventory_string += "and a " + self.inventory[-1]
        elif len(self.inventory) == 1:
            inventory_string += "a " + self.inventory[0]
        else:
            inventory_string += "nothing"
        print("You are carrying " + inventory_string + ".\n")
               
    def add_to_inventory(self):
        if map1.have_rope == True:
            if "rope" not in self.inventory:
                self.inventory.append("rope")
        if map1.have_grapple == True:
            if "grappling hook" not in self.inventory:
                self.inventory.append("grappling hook")
        if map1.have_map == True:
            if "map" not in self.inventory:
                self.inventory.append("map")
        if map1.have_pickaxe == True:
            if "pickaxe" not in self.inventory:
                self.inventory.append("pickaxe")

    def use(self, item, target = None):

        if item == "map":
            if map1.have_map == True:
                map1.print_map_with_player()
            else:
                print_line("You don't have a map.\n")
        elif item == "pickaxe" or item == "A":
            if map1.have_pickaxe == True:
                if target == "rubble" or target == "B":

                    if map1.map[map1.player_y][map1.player_x + 1] == 'B':
                        print_line("You use the pickaxe to clear the rubble. You can now go east.\n")
                        map1.map[map1.player_y][map1.player_x + 1] = ' '
                        if map1.current_level == 0:
                            map1.start_map[map1.player_y][map1.player_x + 1] = ' '
                        elif map1.current_level == 1:
                            map1.up_1_map[map1.player_y][map1.player_x + 1] = ' '
                        elif map1.current_level == -1:
                            map1.down_1_map[map1.player_y][map1.player_x + 1] = ' '

                    elif map1.map[map1.player_y][map1.player_x - 1] == 'B':
                        print_line("You use the pickaxe to clear the rubble. You can now go west.\n")
                        map1.map[map1.player_y][map1.player_x - 1] = ' '
                        if map1.current_level == 0:
                            map1.start_map[map1.player_y][map1.player_x - 1] = ' '
                        elif map1.current_level == 1:
                            map1.up_1_map[map1.player_y][map1.player_x - 1] = ' '
                        elif map1.current_level == -1:
                            map1.down_1_map[map1.player_y][map1.player_x - 1] = ' '

                    elif map1.map[map1.player_y + 1][map1.player_x] == 'B':
                        print_line("You use the pickaxe to clear the rubble. You can now go south.\n")
                        map1.map[map1.player_y + 1][map1.player_x] = ' '
                        if map1.current_level == 0:
                            map1.start_map[map1.player_y + 1][map1.player_x] = ' '
                        elif map1.current_level == 1:
                            map1.up_1_map[map1.player_y + 1][map1.player_x] = ' '
                        elif map1.current_level == -1:
                            map1.down_1_map[map1.player_y + 1][map1.player_x] = ' '

                    elif map1.map[map1.player_y - 1][map1.player_x] == 'B':
                        print_line("You use the pickaxe to clear the rubble. You can now go north.\n")
                        map1.map[map1.player_y - 1][map1.player_x] = ' '
                        if map1.current_level == 0:
                            map1.start_map[map1.player_y - 1][map1.player_x] = ' '
                        elif map1.current_level == 1:
                            map1.up_1_map[map1.player_y - 1][map1.player_x] = ' '
                        elif map1.current_level == -1:
                            map1.down_1_map[map1.player_y - 1][map1.player_x] = ' '

                else:
                    print_line("You can't use the pickaxe on that.\n")
            else:
                print_line("You don't have a pickaxe.\n")

        else:
            print_line("You don't have that item.\n")

    def help(self):
        print_line("Hey there {name}, hope you're still ok down there! Here's a list of things you can do to try and escape.\n".format(name = self.name))
        print_line("You will be able to move around the cave by typing the direction you want to go in. For example, 'north' or 'south'.\n")
        print_line("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
        print_line("You can use items by typing 'use' and then the name of the 'item' and the 'target' for the item's use (if required). For example, 'use' then 'map', or 'use' then 'pickaxe rubble'\n")
        print_line("You can also type 'help' to see this list of commands again.\n")
        print_line("You can type 'quit' to quit the game at any time.\n")
        print_line("Good luck friend, hope you escape!\n")

    def quit(self):
        print_line("You quit the game.")
        exit()

player = Player()

ascii_banner = pyfiglet.figlet_format("The Cave")
print(ascii_banner)
print_line_input("Welcome to The Cave! You have fallen into a cave in a remote location and must find your way out. Good luck!")
print_line_input("You will be able to move around the cave by typing the direction you want to go in. For example, 'north' or 'south'.")
print_line_input("You can also type 'look' to look around the room you are in and 'inventory' to see what you are carrying.")
print_line_input("You can use items by typing 'use' and then the name of the 'item' and the 'target' for the item's use (if required). For example, 'use' then 'map', or 'use' then 'pickaxe rubble'.")
print_line_input("You can also type 'help' to see this list of commands again.")
print_line_input("You can type 'quit' to quit the game at any time.")
print_line_input("Press enter to begin.")
os.system('cls')

opening_banner = pyfiglet.figlet_format("Welcome to The Cave!")
print(opening_banner)
sleep(0.5)

print_line_input("You wake up in a dark cave. You can't remember how you got here or where you are. You can't see anything, but you can feel something next to you on the ground.")
print_line_input("You take the item out of your pocket and feel it. It's a lantern! You can use this to see in the dark. You light the lantern and look around.")
print_line_input("You can see a short distance around yourself from the dim lantern light. You are lying in the centre of a large cavern, with the evening sun shining dimly through a hole in the ceiling far above.")
print_line_input("You can dimly make out a tattered rope hanging down from the hole in the ceiling.")
print_line_input("Suddenly, you hear static coming from your pocket. You take out the radio and hear a voice.")
print_line_input("'KRRRRSSSSSHZZZZZTTHZZZZZ...Hello? Is anyone there?...KRRRRSSSSSHZZZZZTTHZZZZZ...He...KRRRRSSSSSHZZZZZTTHZZZZZ...Hello...yone the...KRRRSSHHT'")
print_line_input("You pick up the radio and say 'Hello'.")
print_line_input("'KRRRRSSH Hello! Wow someone can hear me! I'm so glad! I heard a loud noise and thought someone must be down there!'")
print_line("'What's your name?'\n")
player.name = input("Please enter your name: ")
print_line_input("'Wow I can't believe I found you {name}! I'm so glad you're okay! I think I can see you moving below'. You see a figure waving at you far above.".format(name = player.name))
print_line_input("'I'm going to try and find a way to get you out of there. I'll be back soon!'")
print_line_input("The radio goes silent. You are alone in the cave. You need to find a way out.")
print_line_input("Press Enter to continue.")
os.system('cls')

map1.print_area_around_player()

while player.is_alive == True:
    action = input("Please enter a command: ")
    os.system('cls')
    if action.lower() == "north" or action.lower() == "south" or action.lower() == "east" or action.lower() == "west" or action.lower() == "n" or action.lower() == "s" or action.lower() == "e" or action.lower() == "w":
        map1.move(action)
        map1.change_level()
        map1.print_area_around_player()
        player.add_to_inventory()
    elif action.lower() == "look" or action.lower() == "l":
        player.look()
        map1.print_area_around_player()
    elif action.lower() == "inventory" or action.lower() == "i":
        player.check_inventory()
        map1.print_area_around_player()
    elif action.lower() == "use" or action.lower() == "u":
        item, *target = input("Please enter an item and target (if required): ").split()
        if item.lower() == "map":
            player.use(item)
        else:
            if len(target) == 0 and item in player.inventory:
                print_line("You need to specify a target for that item.\n")
                map1.print_area_around_player()
            elif len(target) == 0:
                print_line("You need to define a target for that item.\n")
                map1.print_area_around_player()
            else:
                player.use(item, target[0])
                map1.print_area_around_player()
    elif action.lower() == "help" or action.lower() == "h":
        player.help()
        map1.print_area_around_player()
    elif action.lower() == "quit" or action.lower() == "q":
        input("Are you sure you want to quit? (Press enter to confirm)")
        player.quit()
    else:
        print_line("I don't understand that command. Please try again.\n")
        map1.print_area_around_player()