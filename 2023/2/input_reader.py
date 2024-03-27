class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.input = []

        for line in self.file:
            line = line.split(":")
            line = line[1]
            line = line.split(";")

            self.input.append(line)

    def get_data(self):
        return self.input
