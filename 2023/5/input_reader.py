class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()


    def convert_to_list(self):
        self.maps = list() 
        self.seeds = list()

        for line in self.file:
            if "seeds:" in line:
                self.seeds = [int(each.strip()) for each in line.strip("seeds:").split()]
                continue
                
            if len(line.split()) == 2:
                self.maps.append(list())
            if len(line.split()) == 3:
                self.maps[-1].append(list(int(each) for each in line.split()))

    def get_data(self):
        return [self.seeds, self.maps]
