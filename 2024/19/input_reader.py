class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = {"patterns": [], "designs": []}

        for i, line in enumerate(self.file):
            if i == 0:
                line = line.strip().split(", ")
                for pattern in line:
                    self.data["patterns"].append(pattern)

            elif i == 1:
                continue
            else:
                line = line.strip()
                self.data["designs"].append(line)

    def get_data(self):
        return self.data
