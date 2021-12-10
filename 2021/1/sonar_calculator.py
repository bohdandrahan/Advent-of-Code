
class Sonar_Calculator():
    def __init__(self, data_list):
        self.data = data_list;

    def calculate1(self):
        return self.calculate(self.data)
    
    def calculate(self, data):
        num_of_increses = 0;
        previous = float('inf');
        if data:
            for each in data:
                each = int(each)
                if each>previous:
                    num_of_increses += 1;
                previous = each;
            return num_of_increses

    def calculate2(self):
        self.get_list_of_triplets();
        return self.calculate(self.triplets);

    def get_list_of_triplets(self):
        self.triplets = [];
        for each in range(len(self.data)-2):
            self.triplets.append(int(self.data[each]) + int(self.data[each+1]) + int(self.data[each+2]));