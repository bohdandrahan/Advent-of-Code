class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):

        self.data = []

        for i, line in enumerate(self.file):
            record_str = line.split()[0]
            record_nums = [int(each)
                           for each in line.split()[1].strip().split(',')]

            self.data.append([record_str, record_nums])

    def get_data(self):
        return self.data
