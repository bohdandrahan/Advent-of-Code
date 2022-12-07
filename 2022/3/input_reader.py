class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()
    def convert_to_list(self):
        self.input = []
        for line in self.file:
            self.input.append([])
            line = line.strip()
            half = int((len(line)+1)/2)

            left = []
            for each in line[0:half]:
                left.append(each)

            right = []
            for each in line[half:]:
                right.append(each)

            self.input[-1] = [left, right]


    def get_list(self):
        return self.input

    def printme(self):
        print(self.input)
