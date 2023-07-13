class Map():
    def __init__(self, player_x = 34, player_y = 14):
        self.height = 30
        self.width = 80
        self.player_x = player_x
        self.player_y = player_y
        self.map = """
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC    R CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC                                      CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC          CCCCCCCCCCCCCCCCCCCCCC      CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC          CCCCCCCCCCCCCCCCCCCCCC      CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCC                     CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC          CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC   CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC                  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCC  R       CCCCCCCCC                  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCC          wwwwCwwww        CC        CCCCCCCCCCCCCCCCCCCCC         C
        CCCCCCCCCCCC          wwwwwwwww   u    CC                                      C
        CCCCCCCCCCCC          wwwwCwwww        CC        CCCCCCCCCCCCCCCCCCCCC         C
        CCCCCCCCCCCC          CCCCCCCCC                  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC                  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC                  CCCCCCC                  CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCH                 CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCC                  CCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC           CCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCC
        CCCC                 CCCCCCCCCCCCCCC           CCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCC
        CCCC R                                         CCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCC
        CCCC                 CCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCC         CCCCC
        CCCC                 CCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCC         CCCCC
        CCCC                 CCCCCCCCCCCCCCCCCCCC     CCCCCCCCCCCCCCCCCCCC         CCCCC
        CCCC                 CCCCCCCCCCCCCCCCCCCC                                  CCCCC
        CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
        """

    def __repr__(self):
        return "Map(height = {height}, width = {width}, player_x = {player_x}, player_y = {player_y})".format(height = self.height, width = self.width, player_x = self.player_x, player_y = self.player_y)
    
    def move_player(self, direction):
        if direction == "north":
            self.player_y -= 1
        elif direction == "south":
            self.player_y += 1
        elif direction == "east":
            self.player_x += 1
        elif direction == "west":
            self.player_x -= 1
        else:
            print("Invalid direction")
            return
        if self.player_x < 0:
            self.player_x = 0
        elif self.player_x >= self.width:
            self.player_x = self.width - 1
        if self.player_y < 0:
            self.player_y = 0
        elif self.player_y >= self.height:
            self.player_y = self.height - 1
        print("You are now at ({x}, {y})".format(x = self.player_x, y = self.player_y))
        

    def print_map(self):
        for row in self.map:
            print(row)

    def print_map_with_player(self):
        for i, row in enumerate(self.map):
            if i == self.player_y:
                print(row[:self.player_x] + "P" + row[self.player_x + 1:])
            else:
                print(row)

map = Map()
for i in range(50):
    print(map.map[i][i])