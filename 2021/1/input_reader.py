class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path);
        self.convert_to_list();

    
    def convert_to_list(self):
        self.input = [];
        for line in self.file:
            self.input.append(line.strip())
    def get_list(self):
        return self.input
