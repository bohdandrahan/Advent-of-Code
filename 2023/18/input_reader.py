class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = []
        for i, line in enumerate(self.file):
            self.data.append(line.strip().split(" "))

        self.data = [[each[0], int(each[1]), each[2]] for each in self.data]

    def get_data(self):
        return self.data
