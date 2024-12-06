class Calculator():
    def __init__(self, data):
        self.data = data
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        self.current_direction: int = 0  # index of self.directions
        self.current_position: list[int]
        self.current_data = data[:]

    def calculate1(self):
        print('calculate 1 is running')

        visited_map = [[val == '^' for val in row] for row in self.data]

        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                if self.data[x][y] == "^":
                    self.current_position = [x, y]

        while True:
            next_x = self.current_position[0] + \
                self.directions[self.current_direction][0]

            next_y = self.current_position[1] + \
                self.directions[self.current_direction][1]

            if next_x < 0 or next_x >= len(self.data) or next_y < 0 or next_y >= len(self.data[0]):
                break

            if self.data[next_x][next_y] == "#":
                self.change_direction()

            else:
                visited_map[self.current_position[0]
                            ][self.current_position[1]] = True

                self.current_position = [next_x, next_y]

        result = sum(sum(row) for row in visited_map) + 1

        return result

    def calculate2(self):
        print('calculate 2 is running')
        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                if self.data[x][y] == "^":
                    self.current_position = [x, y]
                    self.init_position = [x, y]
        sum = 0

        for x in range(len(self.data)):
            for y in range(len(self.data[0])):
                print(x, y)

                self.current_position = self.init_position
                self.current_direction = 0
                if self.current_position == [x, y]:
                    continue

                if self.data[x][y] == "#":
                    continue

                self.current_data = [[item for item in row]
                                     for row in self.data]
                self.current_data[x][y] = "#"

                visited_map = set()

                while True:
                    next_x = self.current_position[0] + \
                        self.directions[self.current_direction][0]

                    next_y = self.current_position[1] + \
                        self.directions[self.current_direction][1]

                    if next_x < 0 or next_x >= len(self.current_data) or next_y < 0 or next_y >= len(self.current_data[0]):
                        break

                    if self.current_data[next_x][next_y] == "#":
                        self.change_direction()

                    elif tuple([self.current_position[0], self.current_position[1], self.current_direction]) in visited_map:
                        sum += 1
                        break

                    else:
                        visited_map.add(tuple(
                            [self.current_position[0], self.current_position[1], self.current_direction]))
                        self.current_position = [next_x, next_y]

        return sum

    def change_direction(self):
        self.current_direction = (self.current_direction+1) % 4
