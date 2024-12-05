class Calculator():
    def __init__(self, data):
        self.data = data
        self.directions = [[1, 0], [1, 1],
                           [0, 1], [-1, 1],
                           [-1, 0], [-1, -1],
                           [0, -1], [1, -1]]
        self.word = 'XMAS'
        self.possible_permutations = ["MMSS", "SMMS", "SSMM",
                                      "MSSM"]
        self.diagonal_directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

    def calculate1(self):
        print('calculate 1 is running')
        sum = 0

        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                for direction in self.directions:
                    if self.get_is_word(x, y, direction):
                        sum += 1

        return sum

    def calculate2(self):
        print('calculate 2 is running')

        sum = 0

        print('calculate 1 is running')
        sum = 0

        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                for possible_permutation in self.possible_permutations:
                    if self.data[x][y] != "A":
                        continue
                    if self.get_is_word_cross(x, y, possible_permutation):
                        sum += 1
                        break

        return sum

    def get_is_word_cross(self, x, y, possible_permutation):
        is_word_cross = False

        for i, direction in enumerate(self.diagonal_directions):
            if x + direction[0] >= len(self.data[0]) or x + direction[0] < 0 \
                    or y + direction[1] >= len(self.data) or y + direction[1] < 0:
                break

            if self.data[x + direction[0]][y + direction[1]] != possible_permutation[i]:
                break

            if i == 3:
                is_word_cross = True

        return is_word_cross

    def get_is_word(self, x, y, direction):
        is_word = True

        for i in range(len(self.word)):
            if x >= len(self.data[0]) or x < 0 \
                    or y >= len(self.data) or y < 0:
                is_word = False
                break

            if self.data[x][y] != self.word[i]:
                is_word = False
                break

            x += direction[0]
            y += direction[1]
        return is_word
