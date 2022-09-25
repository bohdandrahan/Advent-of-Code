
class Fish_Calculator():
    def __init__(self, data_list):
        self.data = data_list;
        self.num_of_gens = 256;

    def run_one_gen(self, pop):
        next_gen = []
        for fish in pop:
            if fish > 0:
                next_gen.append(fish-1)
            else:
                next_gen += [6,8]
        return next_gen

    def run_all_gens(self):
        self.population = self.data
        for i in range(self.num_of_gens):
            print("gen:", i)
            self.population = self.run_one_gen(self.population);

        print("pop: ", len(self.population))
