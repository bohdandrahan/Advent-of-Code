class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        sum = 0
        for word in self.data:
            curr = 0
            for char in word:
                curr += ord(char)
                curr = 17*curr
                curr = curr % 256
            sum += curr
        return sum

    def calculate2(self):
        pass
