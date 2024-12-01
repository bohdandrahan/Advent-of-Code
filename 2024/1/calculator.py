class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        print('calculate 1 is running')

        self.data[0].sort()
        self.data[1].sort()

        sum = 0
        for i, each in enumerate(self.data[0]):
            sum += abs(self.data[0][i] - self.data[1][i])
        return sum

    def calculate2(self):
        print('calculate 2 is running')

        print(self.data[0].count(3))

        result = 0
        for each in self.data[0]:
            result += each*self.data[1].count(each)
        return result

        pass
