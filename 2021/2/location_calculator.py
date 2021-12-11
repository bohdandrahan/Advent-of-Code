
class Location_Calculator():
    def __init__(self, input_list):
        self.input_list = input_list;
        self.calculate1();
    
    def calculate1(self):
        self.horizontal_pos = 0;
        self.depth = 0;
        for each in self.input_list:
            if each[0] == 'up':
                self.depth -= each[1];
            if each[0] == 'down':
                self.depth += each[1];
            if each[0] == 'forward':
                self.horizontal_pos += each[1];

    def calculate2(self):
        self.horizontal_pos = 0;
        self.depth = 0;
        self.aim = 0;
        for each in self.input_list:
            if each[0] == 'up':
                self.aim -= each[1];
            if each[0] == 'down':
                self.aim += each[1];
            if each[0] == 'forward':
                self.horizontal_pos += each[1];
                self.depth += self.aim * each[1];



    def get_horizontal_pos(self):
        return self.horizontal_pos;

    def get_depth(self):
        return self.depth;

    def get_result(self):
        return self.get_depth() * self.get_horizontal_pos()
    
    def print_result(self):
        print ('--Result:-- \n Depth = ' + str(self.get_depth())
               + "\n Horizontal position = " + str(self.get_horizontal_pos())
               + '\n Product of multiplication = ' + str(self.get_result()));