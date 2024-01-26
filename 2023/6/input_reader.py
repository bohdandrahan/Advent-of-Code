class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()


    def convert_to_list(self):
        self.times = list() 
        self.distances = list()

        for line in self.file:
            if "Time:" in line:
                self.times = [int(each.strip()) for each in line.strip("Time:").split()]

            if "Distance:" in line:
                self.distances = [int(each.strip()) for each in line.strip("Distance:").split()]
                

    def get_data(self):
        return [self.times, self.distances]
