class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()


    def convert_to_list(self):
        self.input = []

        for line in self.file:
            line = line.split(':')[1].split('|')
            
            winning_nums = list(map(int, line[0].split()))
            nums_you_have = list(map(int, line[1].split()))

            self.input.append([winning_nums, nums_you_have])

    def get_list(self):
        return self.input
