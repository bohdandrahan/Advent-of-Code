
class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):

        total = self.data[0].sum()

        return total

    def calculate2(self):
        hash = set()

        frequency = 0

        while True:
            for each in self.data[0]:
                frequency += each

                if frequency in hash:
                    return frequency
                else:
                    hash.add(frequency)
