# Create a class that allows you to create a map object and then move a player around on it
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
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
                    ['C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C']]
        self.blank_map = [['?'] * 20] * 20
        self.height = len(self.map)
        self.width = len(self.map[0])

    def __repr__(self):
        return "Map(height = {height}, width = {width}, player_x = {player_x}, player_y = {player_y})".format(height = self.height, width = self.width, player_x = self.player_x, player_y = self.player_y)
    
    # def move(self, direction):
    #     if direction == 'north':
    #         new_cell = self.map[self.player_y - 1][self.player_x]
    #         if new_cell == ' ':
    #             self.player_y -= 1
    #         elif new_cell == 'R':
    #             print("You found a rope!")
    #             self.player_y -= 1
    #         else:
    #             print("You can't go that way")

    def north(self):
        new_cell = self.map[self.player_y - 1][self.player_x]
        if new_cell == ' ':
            self.player_y -= 1
        elif new_cell == 'R':
            print("You found a rope!")
            self.player_y -= 1
        else:
            print("You can't go that way")

    def south(self):
        new_cell = self.map[self.player_y + 1][self.player_x]
        if new_cell == ' ':
            self.player_y += 1
        elif new_cell == 'R':
            print("You found a rope!")
            self.player_y += 1
        else:
            print("You can't go that way")

    def east(self):
        new_cell = self.map[self.player_y][self.player_x + 1]
        if new_cell == ' ':
            self.player_x += 1
        elif new_cell == 'R':
            print("You found a rope!")
            self.player_x += 1
        else:
            print("You can't go that way")
    
    def west(self):
        new_cell = self.map[self.player_y][self.player_x - 1]
        if new_cell == ' ':
            self.player_x -= 1
        elif new_cell == 'R':
            print("You found a rope!")
            self.player_x -= 1
        else:
            print("You can't go that way")
        
    def print_map(self):
        map_string = ""
        for row in self.map:
            for char in row:
                map_string += char
            map_string += "\n"
        print(map_string)

    def print_map_with_player(self):
        map_string = ""
        for i, row in enumerate(self.map):
            for j, char in enumerate(row):
                if i == self.player_y and char == ' ' and j == self.player_x:
                    map_string += 'P'
                else:
                    map_string += char
            map_string += "\n"
        print(map_string)

map1 = Map()