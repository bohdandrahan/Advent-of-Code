from tkinter import SEL_FIRST

class Input_Reader():
    #$ cd .. 
    #$ cd <foldername>
    #$ ls
    #<int> <filename>
    #dir <dirname>

    #
    def __init__(self,file_path):
        self.file = open(file_path)
        input = []
        for line in self.file:
            input.append(line.strip())
        self.commands = input


    def printme(self):
        print(self.commands)
