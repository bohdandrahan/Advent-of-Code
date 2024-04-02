
import sys
sys.setrecursionlimit(20000)


class Calculator():
    def __init__(self, data):
        self.data = data
        self.directions = {
            'up': [-1, 0], 'right': [0, 1], 'down': [1, 0], 'left': [0, -1]}

    def out_of_bound(self, location):
        if location[0] < 0 or location[0] >= len(self.data[0]):
            return True
        if location[1] < 0 or location[1] >= len(self.data):
            return True
        return False

    def get_next_location(self, location, dir):
        # print(dir, location)
        new_location = [location[0] + self.directions[dir]
                        [0], location[1] + self.directions[dir][1]]

        return new_location

    def get_char(self, location):
        return self.data[location[0]][location[1]]

    def calculate(self, curr):

        total_seen = set()
        total_seen_dir = set()

        def go(curr, path):
            # print(curr, '<- CURR')
            next_location = self.get_next_location(curr[0], curr[1])
            if self.out_of_bound(next_location):
                # print(curr, 'OUT OF BOUND')
                return

            total_seen.add(tuple(next_location))

            path = list(path)

            if tuple([curr[0][0], curr[0][1], curr[1]]) in total_seen_dir:
                return

            total_seen_dir.add(tuple([curr[0][0], curr[0][1], curr[1]]))
            path.append(curr)

            if self.get_char(next_location) == '\\' \
                    or self.get_char(next_location) == '/' \
                    or self.get_char(next_location) == '.':

                next_dir = curr[1]

                if self.get_char(next_location) == '\\':
                    # print('BACKSLASH \\')
                    if curr[1] == 'up':
                        next_dir = 'left'
                    elif curr[1] == 'right':
                        next_dir = 'down'
                    elif curr[1] == 'down':
                        next_dir = 'right'
                    elif curr[1] == 'left':
                        next_dir = 'up'
                    else:
                        print('Incorrect direction')
                        return

                if self.get_char(next_location) == '/':
                    # print('/ is reached', curr[1])
                    if curr[1] == 'up':
                        next_dir = 'right'
                    elif curr[1] == 'right':
                        next_dir = 'up'
                    elif curr[1] == 'down':
                        next_dir = 'left'
                    elif curr[1] == 'left':
                        next_dir = 'down'
                    else:
                        print('Incorrect direction')
                        return

                go([next_location, next_dir], path)

            # print('BEFORE IF GO -')
            if self.get_char(next_location) == '-':
                # print('GO -')
                go([next_location, 'right'], path)
                go([next_location, 'left'], path)

            if self.get_char(next_location) == '|':
                # print('GO |')
                go([next_location, 'up'], path)
                go([next_location, 'down'], path)

            # print(self.get_char(next_location), 'END OF GO')

        go(curr, [])

        return (total_seen)

    def calculate1(self):
        total_seen = self.calculate([[0, -1], 'right'])

        return len(total_seen)

    def calculate2(self):
        max_total_seen = -1
        for i in range(len(self.data)):
            max_total_seen = max(
                max_total_seen, len(self.calculate([[i, -1], 'right'])))

            max_total_seen = max(max_total_seen, len(self.calculate(
                [[i, len(self.data[0])], 'left'])))

        for j in range(len(self.data[0])):
            max_total_seen = max(
                max_total_seen, len(self.calculate([[-1, j], 'down'])))

            max_total_seen = max(max_total_seen, len(self.calculate(
                [[len(self.data), j], 'up'])))

            pass
        return max_total_seen
