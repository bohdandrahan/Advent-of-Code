class Calculator():

    def __init__(self, data, debugger = False):
        self.data = data
        self.debugger = debugger


    def calculate1(self):
        print('calculate 1 is running')
        return 

    def calculate2(self):
        print('calculate 2 is running')

        return
    
    def pr(self, content_to_print):
        if self.debugger:
            print(content_to_print)