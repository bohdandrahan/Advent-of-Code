class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path);
        self.convert_to_list();

    
    def convert_to_list(self):
        self.input = [];
        for line in self.file:
            self.input.append(line.split());
            self.input[-1][1]=int(self.input[-1][1])
        
    def get_list(self):
        return self.input
