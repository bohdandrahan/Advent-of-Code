class Input_Reader():
    def __init__(self,file_path):
        self.file = open(file_path)
        self.convert_to_list()


    def convert_to_list(self):

        self.data = {'nodes' : {}, 'rules' : ''}
        
        for i, line in enumerate(self.file):
            if i == 0:
                self.data['rules'] = line.strip()
            elif i > 1:
                node = line[0:3]
                left = line[7:10]
                right = line[12:15]

                self.data['nodes'][node] = [left, right]

    def get_data(self):
        return self.data
