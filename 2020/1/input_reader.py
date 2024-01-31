class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_data()

    def convert_data(self):

        self.data = []
        for line in self.file:
            self.data.append(int(line.strip()))

    def get_data(self):
        return self.data
