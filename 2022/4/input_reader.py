class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.input = []

        for line in self.file:

            line = line.strip().split(",")

            self.input.append([])
            for i, each in enumerate(line):
                if i%2 == 0 and i != 0:
                    self.input.append([])

                self.input[-1].append(list(eval(i) for i in each.split("-")))

    def get_list(self):
        return self.input

    def printMe(self):
        print(self.input)
