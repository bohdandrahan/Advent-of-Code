class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):

        current = []
        self.data = []

        for i, line in enumerate(self.file):
            if line == '\n':
                self.data.append(current)
                current = []

            else:
                current.append(line.strip())

        self.data.append(current)

    def get_data(self):
        return self.data
