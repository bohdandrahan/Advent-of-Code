from tkinter import SEL_FIRST


class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_crates()
        self.convert_commands()


    def convert_crates(self):

        crates = []
        for line in self.file:
            if len(crates) == 0:
                crates = [[] for i in range(len(line)//4)]

            group_size = 4
            unformated_line = [line[i:i+group_size] for i in range(0, len(line), group_size)]
            if unformated_line[0][1].isdigit():
                break #it is no longer a row of crates

            for i, crate in enumerate(unformated_line):
                if(crate[1] != " "):
                    crates[i].insert(0, crate[1])
                
            self.crates = crates

    def convert_commands(self):
        self.file.readline() #skip empty line

        commands = []
        instructions = ['move', 'from', 'to']
        for line in self.file:
            commands.append([i.strip() for i in line.split(' ') if i not in instructions])
        self.commands = commands

    def get_crates(self):
        return self.crates

    def get_commands(self):
        return self.commands

    def printme(self):
        print("CRATES", self.crates)
        print("COMMANDS", self.commands)
