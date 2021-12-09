class Sonar_Calculator():
    def __init__(self, data_list):
        self.data = data_list;

    def calculate(self):
        num_of_increses = 0;
        previous = 0;
        if self.data:
            for each in self.data:
                each = int(each)
                if each>previous:
                    num_of_increses += 1;
                previous = each;
            return num_of_increses

