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
                          ['C','LU',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C',' ',' ',' ','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C',' ',' ',' ','LD','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                          ['C','C','C','C','C','C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','LD','C','C','C','C','C','C','C','C','C'],
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
                          ['C','C','C','C',' ','G','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C'],
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
                            ['C','C',' ','C','C','C','C','C','C','C','LU',' ',' ','C','C','C','C','C','C','C',' ','C','C','C',' ',' ',' ','C','C','C'],
                            ['C','C','M','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','LU','C','C','C','C',' ',' ','C','C','C'],
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
                            ['C','PA',' ',' ',' ',' ','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C',' ','C','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ','C','C','C',' ',' ',' ',' ',' ',' ',' ','C','C','C','C','C'],
                            ['C',' ',' ',' ','C','C','C','C','C','C','C',' ',' ',' ',' ',' ',' ',' ',' ','C','C','C',' ',' ','C','C','C','C','C','C'],
                            ['C',' ',' ','C','C','C','C','C','C','C','C','C',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                            ['C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C']]
        
        self.up_1_map = [['C','C',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','LD',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
                         ['C','C',' ',' ',' ',' ',' ',' ','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C','C'],
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
        self.have_map = True
        

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
        elif self.map[y-1][x] == 'PA':
            can_move_directions.append('north to pick up a pickaxe')

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
        elif self.map[y + 1][x] == 'PA':
            can_move_directions.append('south to pick up a pickaxe')
            
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
        elif self.map[y][x + 1] == 'PA':
            can_move_directions.append('east to pick up a pickaxe')
            
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
        elif self.map[y][x - 1] == 'PA':
            can_move_directions.append('west to pick up a pickaxe')
            
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
                self.inventory.append('rope')
                self.have_rope = True
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
                self.player_y -= 1
                self.map[self.player_y][self.player_x] = ' '
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
            elif new_cell == 'PA':
                print("You found a pickaxe!")
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
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
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
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
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
            elif new_cell == 'B':
                print("The way is blocked by rubble, you'll need something to clear it with.")
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
        player_map = [self.map[self.player_y - 1][self.player_x - 1:self.player_x + 1],
                      self.map[self.player_y][self.player_x - 1:self.player_x + 1],
                      self.map[self.player_y + 1][self.player_x - 1:self.player_x + 1]]
        for i, row in enumerate(player_map):
            for j, char in enumerate(row):
                if i == 1 and j == 1:
                    map_string += 'P'
                else:
                    map_string += char
            map_string += "\n"
        print(map_string)
            



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
        print_line("You can use items by typing 'use' and then the name of the 'item' and the 'target' for the item's use.\n")
        print_line("You can also type 'help' to see this list of commands again.\n")
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
# print_line_input("You can use items by typing 'use' and then the name of the item. For example, 'use lantern'.")
# print_line_input("You can also type 'help' to see this list of commands again.")
# print_line_input("You can type 'quit' to quit the game at any time.")
# print_line_input("Press enter to begin.")
os.system('cls')

#map1.print_area_around_player()

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
        map1.print_area_around_player()
    elif action == "look":
        player.look()
    elif action == "inventory":
        player.check_inventory()
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
    elif action == "quit":
        player.quit()
    elif action == "print1":
        print("This is working")
    else:
        print_line("I don't understand that command. Please try again.\n")