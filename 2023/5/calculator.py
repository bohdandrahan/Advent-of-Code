
class Calculator():
    def __init__(self, data):
        self.seeds = data[0]
        self.maps = data[1]

    def calculate1(self):
        seeds = self.seeds[:]
        for map in self.maps:
            for i, seed in enumerate(seeds):
                for row in map:
                    if row[1] <= seed <=row[1]+row[2]:
                        seeds[i] = row[0] - row[1] + seed
        
        print(min(seeds))
        return min(seeds)
    
    #correct in theory, is able to crack the example input. it will take forever to compute the real data. need to optimize
    def calculate2(self):
        seeds = []
        for i in range(0, len(self.seeds), 2):
            seeds.extend(range(self.seeds[i], self.seeds[i]+self.seeds[i+1]))
        
        for map in self.maps:
            for i, seed in enumerate(seeds):
                for row in map:
                    if row[1] <= seed <=row[1]+row[2]:
                        seeds[i] = row[0] - row[1] + seed
                        break
        
        print(min(seeds))
        return min(seeds)