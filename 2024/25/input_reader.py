from typing import DefaultDict


class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = DefaultDict(list)

        current_element = list()
        for i, line in enumerate(self.file):
            line = line.strip()
            if not line:
                if current_element[0].count("#") == 5:
                    self.data["locks"].append(current_element)
                else:
                    self.data["keys"].append(current_element)
                current_element = []
            else:
                current_element.append(line)

        if current_element[0].count("#") == 5:
            self.data["locks"].append(current_element)
        else:
            self.data["keys"].append(current_element)
        current_element = []

    def get_data(self):
        return self.data
