class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path);
        self.data = []
        self.convert_data();

    def convert_data(self):

        row = []
        for line in self.file:
            string_num = str(line.strip())
            mapObject = map(int, string_num)
            row = list(mapObject)

            self.data.append(row)
        print(self.data)

    def get_data(self):
        return self.data
