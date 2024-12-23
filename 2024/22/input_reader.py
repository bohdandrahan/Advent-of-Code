class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = list()

        for i, line in enumerate(self.file):
            line = int(line.strip())
            self.data.append(line)

    def get_data(self):
        return self.data
