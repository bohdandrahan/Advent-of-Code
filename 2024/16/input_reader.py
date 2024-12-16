class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = {"map": [], "start_pos": [], "end_pos": []}

        for x, line in enumerate(self.file):
            line = line.strip()
            self.data["map"].append(line)

            for y, tile in enumerate (line):
                if tile == "S":
                    self.data["start_pos"] = [x,y]
                if tile == "E":
                    self.data["end_pos"] = [x,y]

    def get_data(self):
        return self.data
