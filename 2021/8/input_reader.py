class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path);
        self.input = {}
        self.convert_to_dict();

    def convert_to_dict(self):
        for line in self.file:
            input = line.split("|")
            key = tuple(input[0].strip().split(" "))
            value = input[1].strip().split(" ")
            self.input[key] = value

    def get_dict(self):
        return self.input
