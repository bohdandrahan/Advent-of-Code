
class Calculator():
    def __init__(self, data):
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

    def regestr_data(self):
        regestry = []
        for x, line in enumerate(self.data):
            for y,  ch in enumerate(line):
                if ch == '#':
                    regestry.append([x, y])

        self.regesrty = regestry

    def regestr(self):
        regestry = []
        for x, line in enumerate(self.expanded_data):
            for y,  ch in enumerate(line):
                if ch == '#':
                    regestry.append([x, y])

        self.regesrty = regestry

    def expanded_regestr(self):
        expanded_data = [[], []]
        for i, line in enumerate(self.data):
            empty = True
            for each in line:
                if each != '.':
                    empty = False

            if empty:
                expanded_data[0].append(i)

        for i in range(len(self.data[0])):

            empty = True
            for j in range(len(self.data)):
                if self.data[j][i] != '.':
                    empty = False

            if empty:
                expanded_data[1].append(i)

        self.expanded_regesrty = expanded_data

    def calculate1(self):
        # This was my solution to part one before part two was available.
        # Now it is obsolete due to the following more generic solution
        # self.expand()
        # self.regestr()
        #
        # sum = 0
        # for i, galaxy in enumerate(self.regesrty):
        #     if i == len(self.regesrty)-1:
        #         continue
        #
        #     for each in self.regesrty[i+1:]:
        #
        #         sum += abs(each[0]-galaxy[0]) + abs(each[1]-galaxy[1])
        #
        # return sum

        return self.calculateWithStep(2)

    def calculate2(self):

        return self.calculateWithStep(1000000)

    def calculateWithStep(self, step):
        self.expanded_regestr()
        self.regestr_data()

        sum = 0
        x = 0
        for i, galaxy in enumerate(self.regesrty):
            if i == len(self.regesrty)-1:
                continue
            for each in self.regesrty[i+1:]:
                x += 1
                for j in range(abs(each[0] - galaxy[0])):
                    if j + min(galaxy[0],
                               each[0]) in self.expanded_regesrty[0]:
                        sum += step
                    else:
                        sum += 1

                for j in range(abs(each[1] - galaxy[1])):
                    if j + min(galaxy[1], each[1]) in self.expanded_regesrty[1]:
                        sum += step
                    else:
                        sum += 1

        return sum
