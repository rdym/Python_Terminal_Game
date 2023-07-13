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
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.blank_map = [['?'] * self.width for _ in range(self.height)]
        

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
    
    def move(self, direction):
        if direction == 'north':
            new_cell = self.map[self.player_y - 1][self.player_x]
            if new_cell == ' ':
                self.player_y -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_y -= 1
                self.reveal_map(self.player_x, self.player_y)
            else:
                print("You can't go that way")
        elif direction == 'south':
            new_cell = self.map[self.player_y + 1][self.player_x]
            if new_cell == ' ':
                self.player_y += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_y += 1
                self.reveal_map(self.player_x, self.player_y)
            else:
                print("You can't go that way")
        elif direction == 'east':
            new_cell = self.map[self.player_y][self.player_x + 1]
            if new_cell == ' ':
                self.player_x += 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x += 1
                self.reveal_map(self.player_x, self.player_y)
            else:
                print("You can't go that way")
        elif direction == 'west':
            new_cell = self.map[self.player_y][self.player_x - 1]
            if new_cell == ' ':
                self.player_x -= 1
                self.reveal_map(self.player_x, self.player_y)
            elif new_cell == 'R':
                print("You found a rope!")
                self.player_x -= 1
                self.reveal_map(self.player_x, self.player_y)
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
        for i, row in enumerate(self.blank_map):
            for j, char in enumerate(row):
                if i == self.player_y and char == ' ' and j == self.player_x:
                    map_string += 'P'
                else:
                    map_string += char
            map_string += "\n"
        print(map_string)

map1 = Map()