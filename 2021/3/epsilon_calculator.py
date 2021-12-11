class Epsilon_Calculator():
    def __init__(self, input_list):
        self.input_list = input_list;
        self.calculate_sums()
        self.calculate_epsilon();
        self.calculate_gamma();
        self.calculate_o2();
        self.calculate_co2();
    
    def calculate_o2():
        self.o2 = str('')
        for each in self.sums:
            if each >= (len(self.input_list)/float(2)):
                self.o2 += str(1);
            else: self.epsilon += str(1);


    
    def calculate_epsilon(self):
        self.epsilon = str('');
        for each in self.sums:
            if each > (len(self.input_list)/float(2)):
                self.epsilon += str(0);
            else: self.epsilon += str(1);

    def calculate_gamma(self):
        self.gamma = str('');
        for each in self.epsilon:
            if each == '0':
                self.gamma += '1';
            else: self.gamma += '0';

    def calculate_sums(self):
        self.sums = [];
        for each in range(len(self.input_list[0])):
            self.sums.append(sum(i[each] for i in self.input_list))

    def print_result(self):
        print('Gamma: '+self.gamma+'\n'+'Epsilon: '+self.epsilon)
        print('Gamma in decimal: ', int(int(self.gamma, 2)))
        print('Epsilon in decimal: ', int(int(self.epsilon, 2)))
        print('Gamma x Epsilon = ', int(self.gamma, 2) * int(self.epsilon, 2))
