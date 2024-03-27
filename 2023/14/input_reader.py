class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = []

        for i, line in enumerate(self.file):
            listline = []
            for char in line:
                if char == '\n':
                    continue
                listline.append(char)
            self.data.append(listline)

    def get_data(self):
        return self.data
