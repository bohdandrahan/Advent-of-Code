
class Calculator():
    def __init__(self, crates, commands):
        self.crates = crates
        self.commands = commands

    def calculate1(self):
        for command in self.commands:
            for i in range(int(command[0])):
                self.crates[int(command[2])-1].append(self.crates[int(command[1])-1].pop())
        return self.get_top_crates()

    def calculate2(self):
        for command in self.commands:
            load = self.crates[int(command[1])-1][-int(command[0]):]
            self.crates[int(command[1])-1] = self.crates[int(command[1])-1][0: -int(command[0])]
            self.crates[int(command[2])-1] = self.crates[int(command[2])-1] + load
        return self.get_top_crates()

    def get_top_crates(self):
        top = ''
        for crate in self.crates:
            top += crate[-1]
        return top


