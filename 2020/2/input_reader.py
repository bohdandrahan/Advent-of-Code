class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_data()

    def convert_data(self):

        self.data = []
        for line in self.file:
            letter = line.split(":")[0][-1]
            rule = line.split(":")[0].split()[0]
            min_letter = int(rule.split("-")[0])
            max_letter = int(rule.split("-")[1])
            password = line.split(":")[1].strip()

            self.data.append([min_letter, max_letter, letter, password])

    def get_data(self):
        return self.data
