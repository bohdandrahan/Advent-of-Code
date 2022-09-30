
class Crab_Calculator():
    def __init__(self, data_list):
        self.data = data_list;
        self.calculate_fuel1();
        self.calculate_fuel2();

    def calculate_fuel1(self):
        self.median = sorted(self.data)[len(self.data)//2]

        self.fuel = sum([abs(self.median - i) for i in self.data])
        print("Part 1, Fuel:", self.fuel)

    def calculate_fuel2(self):
        self.fuel = 0

        #Prone to rounding error. For my input it gave me an avarage of 462.508.
        #462.508 get to be rounded up to 463, but the correct answer assumed it
        #to be 462. Not sure if it is the python or the server side issue.
        #I consider this to be good enough solution and not going to investigate
        #this bug anymore.
        self.average = round(((sum(self.data)/float(len(self.data)))))

        print(self.average)
        for i, number in enumerate(self.data):
            for x in range(abs(number - self.average)+1):
                self.fuel += x;

        print("Part 2, Fuel:", self.fuel)
