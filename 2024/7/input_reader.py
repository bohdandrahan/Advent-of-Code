class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = []
        for i, line in enumerate(self.file):
            line = line.strip().split(':')

            self.data.append([int(line[0]), [int(each)
                             for each in line[1].strip().split()]])

    def get_data(self):
        return self.data
