from line import Line

class Input_Reader():

    def __init__(self,file_path):
        self.file = open(file_path);
        self.lines = list()
        for line in self.file:
            start_point=line.split('->')[0].strip().split(',')
            start_point = list(map(int, start_point))
            end_point =line.split('->')[1].strip().split(',')
            end_point = list(map(int, end_point))
            self.lines.append(Line(start_point, end_point))
    
    def get_lines(self):
        return self.lines

            