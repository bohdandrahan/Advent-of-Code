
class Fish_Calculator():
    def __init__(self, data_list, days):
        self.data = data_list;
        self.num_of_gens = days;

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
        print("days:", self.num_of_gens, "naive method: pop: ", len(self.population))

    def format_dict(self):
        self.dict = {}
        for each in self.data:
            if each in self.dict:
                self.dict[each] += 1
            else:
                self.dict[each] = 1
        for each in range(9):
            if not each in self.dict:
                self.dict[each] = 0

    def run_one_gen_dict(self, pop):
        next_gen = {}
        for i in range(9):
            if i == 0:
                pop[9] = pop[0]
                if 7 in pop:
                    pop[7] += pop[0]

            if i + 1 in pop:
                pop[i] = pop[i+1]
        return pop

    def run_all_gens_dict(self):
        self.format_dict()
        self.population = self.dict

        for i in range(self.num_of_gens):
            self.population = self.run_one_gen_dict(self.population)

        total = 0
        for each in self.population:
            if not each == 9:
                total += self.population[each]
        print("days:", self.num_of_gens, "not naive method, pop:" ,total)
