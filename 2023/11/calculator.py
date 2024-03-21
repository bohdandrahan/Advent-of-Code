

import re


class Calculator():
    def __init__(self, data):
        # TODO: maybe refactor self.analyze_start to be in construcrtors
        # so the value is not being overwritten in methods
        self.data = data

    def expand(self):
        expanded_data = []
        for line in self.data:
            empty = True
            for each in line:
                if each != '.':
                    empty = False

            if empty:
                expanded_data.append(line)

            expanded_data.append(line)

        self.expanded_data = []

        for j in range(len(expanded_data)):
            self.expanded_data.append([])

        for i in range(len(expanded_data[0])):

            empty = True
            for j in range(len(expanded_data)):
                if expanded_data[j][i] != '.':
                    empty = False

            for j in range(len(expanded_data)):
                if empty:
                    self.expanded_data[j].append(expanded_data[j][i])
                self.expanded_data[j].append(expanded_data[j][i])

    def regestr(self):
        regestry = []
        for x, line in enumerate(self.expanded_data):
            for y,  ch in enumerate(line):
                if ch == '#':
                    regestry.append([x, y])

        self.regesrty = regestry

    def calculate1(self):
        self.expand()
        self.regestr()

        sum = 0
        for i, galaxy in enumerate(self.regesrty):
            if i == len(self.regesrty)-1:
                continue

            for each in self.regesrty[i+1:]:
                print('each', each, galaxy, abs(each[0]-galaxy[0]), abs(each[1]-galaxy[1])
                      )
                sum += abs(each[0]-galaxy[0]) + abs(each[1]-galaxy[1])

        return sum

    def calculate2(self):
        pass
