
class Crab_Calculator():
    def __init__(self, data_list):
        self.data = data_list;
        self.calculate_fuel();

    def calculate_fuel(self):
        self.median = sorted(self.data)[len(self.data)//2]

        self.fuel = sum([abs(self.median - i) for i in self.data])
        print(self.fuel)
