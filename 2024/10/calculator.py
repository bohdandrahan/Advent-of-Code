class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        # self.pr(data)

        self.directions = [[0, 1], [1, 0],
                           [0, -1], [-1, 0]]

    def pr(self, *content_to_print):

        if self.debugger:
            print(*content_to_print)

    def calculate1(self):
        print('calculate 1 is running')

        zeros = list()

        for x, row in enumerate(self.data):
            for y, each in enumerate(self.data[x]):
                if each == 0:
                    self.pr(x, y)
                    zeros.append([x, y])

        result = 0
        for zero in zeros:
            nine_map = set()
            self.walk_path(nine_map, 0, zero)
            result += len(nine_map)

        return result

    def walk_path(self, map, current_number, current_location):
        if current_number == 9:
            map.add(tuple(current_location))

        for direction in self.directions:
            next_x = current_location[0] + direction[0]
            next_y = current_location[1] + direction[1]
            if next_x < 0 or next_x >= len(self.data) or next_y < 0 or next_y >= len(self.data[0]):
                continue
            if self.data[next_x][next_y] != current_number + 1:
                continue
            self.walk_path(map, current_number + 1, [next_x, next_y])

    def calculate2(self):
        print('calculate 2 is running')
        return
