class Calculator():
    def __init__(self, data):
        self.data = data

    def rotate_matrix_90_clockwise(self, matrix):
        # Transpose the matrix
        transposed_matrix = list(zip(*matrix))
        # Reverse the columns to get clockwise rotation
        rotated_matrix = [list(row[::-1]) for row in transposed_matrix]

        return rotated_matrix

    def roll(self, data):
        rolled_data = list(data)
        for i, row in enumerate(rolled_data):
            curr = i
            while curr > 0:
                for j, each in enumerate(rolled_data[curr]):
                    if each == 'O':
                        if rolled_data[curr-1][j] == '.':
                            rolled_data[curr-1][j] = 'O'
                            rolled_data[curr][j] = '.'
                curr -= 1

        return rolled_data

    def calculate_value(self, data):
        sum = 0
        i = len(data)-1
        multiplier = 1
        while i >= 0:
            for each in data[i]:
                if each == 'O':
                    sum += multiplier

            multiplier += 1
            i -= 1
        return sum

    def calculate1(self):
        rolled_data = self.roll(self.data)
        return self.calculate_value(rolled_data)

    def calculate2(self):
        curr = self.data

        log = []
        last_indexes = []
        cycle_runs = 500
        progress = 0

        for i in range(cycle_runs):
            if i % (cycle_runs//10) == 0:
                print(f'IN PROGRESS, {progress}% is done')
                progress += 10

            for j in range(4):
                curr = self.roll(curr)
                curr = self.rotate_matrix_90_clockwise(curr)

            if self.calculate_value(curr) in log:
                last_index = log[::-1].index(self.calculate_value(curr))
            else:
                last_index = -1
            last_indexes.append(last_index)
            # print(i, self.calculate_value(curr), last_index)
            log.append(self.calculate_value(curr))
        cycle_len = max(last_indexes[-100:]) + 1
        modulo = (1000_000_000-1) % cycle_len

        for each in range(cycle_runs - 1, -1, -1):
            if each % cycle_len == modulo:
                return log[each]
        return -1
