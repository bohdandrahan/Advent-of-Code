from tkinter import SEL_FIRST


class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.word = self.file.readline()

    def printme(self):
        print(self.word)
