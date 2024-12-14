class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = {"robots": [], "is_test": True}

        for i, line in enumerate(self.file):
            line = line.strip().split(" ")
            position = [int(each) for each in line[0][2:].split(',')]
            velocity = [int(each) for each in line[1][2:].split(',')]
            if position[0] > 20:  # it is rather hacky, but it is so much better than do it manually and I'm sure it will work for all of the posiible inputs

                self.data["is_test"] = False

            self.data["robots"].append(
                {"position": position, "velocity": velocity})

    def get_data(self):
        return self.data
