
class Calculator():

    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):
        self.pr(self.data)
        print('calculate 1 is running')

    def calculate2(self):

        print('calculate 2 is running')

        return
