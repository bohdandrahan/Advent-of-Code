
class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        rolled_data = list(self.data)
        for i, row in enumerate(rolled_data):
            curr = i
            while curr > 0:
                for j, each in enumerate(rolled_data[curr]):
                    if each == 'O':
                        if rolled_data[curr-1][j] == '.':
                            rolled_data[curr-1][j] = 'O'
                            rolled_data[curr][j] = '.'
                curr -= 1

        sum = 0
        i = len(rolled_data)-1
        multiplier = 1
        while i >= 0:
            for each in rolled_data[i]:
                if each == 'O':
                    sum += multiplier

            multiplier += 1
            i -= 1
        return sum

    def calculate2(self):
        pass
