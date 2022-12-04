class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()


    def convert_to_list(self):
        self.input = []
        self.input.append([])
        i = 0
        for line in self.file:
            if(line.strip() == ""):
                i += 1
                self.input.append([])
                continue
            else:
                self.input[i].append(int(line.strip()))

    def get_list(self):
        return self.input
