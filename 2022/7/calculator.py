
import enum


class Calculator():
    def __init__(self, word):
        self.word = word

    def calculate1(self):
        self.n = 4
        return self.calculate()

    def calculate2(self):
        self.n = 14
        return self.calculate()
    
    def calculate(self):
        buff = []
        for i, letter in enumerate(self.word):

            buff.append(letter)
            if len(buff) == self.n + 1:
                buff.pop(0)

            if len(set(buff)) == len(buff) == self.n:
                return i+1



