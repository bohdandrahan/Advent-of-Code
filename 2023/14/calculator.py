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

        for i in range(3):

            for j in range(4):
                curr = self.roll(curr)
                curr = self.rotate_matrix_90_clockwise(curr)
            print(i, self.calculate_value(curr))

        pass
