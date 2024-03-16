

class Calculator():
    def __init__(self, data):
        # TODO: maybe refactor self.analyze_start to be in construcrtors so the value is not being overwritten in methods
        self.data = data
        self.start = self.calculate_start()
        self.legend = {
            '-': [[1, 0], [-1, 0]],
            '|': [[0, 1], [0, -1]],
            'L': [[1, 0], [0, -1]],
            'J': [[-1, 0], [0, -1]],
            '7': [[0, 1], [-1, 0]],
            'F': [[1, 0], [0, 1]]
        }
        self.dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def calculate_start(self):
        for i, row in enumerate(self.data):
            for j, char in enumerate(row):
                if char == 'S':
                    return [j, i]
        return [-1, -1]

    def get_char(self, location):
        x = location[0]
        y = location[1]
        for i, row in enumerate(self.data):
            for j, char in enumerate(row):
                if [j, i] == [x, y]:
                    return char

        return 'char not found'

    def is_valid_position(self, x_y):
        return (x_y[0] >= 0 and x_y[0] < len(self.data)
                and x_y[1] >= 0 and x_y[1] < len(self.data[0]))

    def inverted(self, dir):
        return [-dir[0], -dir[1]]

    def get_next(self, dir, loc):
        return [dir[0]+loc[0], dir[1]+loc[1]]

    def analyze_start(self):
        print('analyze start')
        start_dirs = []
        curr, dir = [], []
        for direction in self.dirs:
            next = self.get_next(direction, self.start)
            if self.is_valid_position(next):
                char = self.get_char(next)
                if char in self.legend \
                        and self.inverted(direction) in self.legend[char]:
                    curr = next
                    dir = direction
                    start_dirs.append(dir)

        for pipe_element in self.legend:
            if start_dirs[0] in self.legend[pipe_element] \
                    and start_dirs[1] in self.legend[pipe_element]:

                self.data[self.start[1]] = pipe_element.join(
                    [self.data[self.start[1]][:self.start[0]],
                     self.data[self.start[1]][self.start[0]+1:]])

        return curr, dir

    def calculate1(self):
        count = 1
        curr, dir = self.analyze_start()
        char = self.get_char(self.start)

        while curr != self.start:
            next_dir = []
            if self.legend[char][0] == self.inverted(dir):
                next_dir = self.legend[char][1]

            else:
                next_dir = self.legend[char][0]

            curr = self.get_next(next_dir, curr)
            char = self.get_char(curr)
            dir = next_dir
            count += 1

        return count//2

    def calculate2(self):

        pipes = [self.calculate_start()]
        curr, dir = self.analyze_start()

        char = self.get_char(self.start)

        print('start found, walking throught the pipe')

        while curr != self.start:
            pipes.append(curr)
            next_dir = []
            if self.legend[char][0] == self.inverted(dir):
                next_dir = self.legend[char][1]

            else:
                next_dir = self.legend[char][0]

            curr = self.get_next(next_dir, curr)
            char = self.get_char(curr)
            dir = next_dir

        print('loop found')

        # there used to be more code here, but this works
        edges = pipes

        print('edges calculated, get area')

        area = 0
        for i in range(len(edges)):
            j = (i + 1) % len(edges)
            area += (edges[i][0] * edges[j][1]) - \
                (edges[j][0] * edges[i][1])

        area = abs(area)/2
        print(area)

        i = area - len(edges)/2 + 1

        return i
