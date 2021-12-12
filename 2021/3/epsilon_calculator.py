class Epsilon_Calculator():
    def __init__(self, input_list):
        self.input_list = input_list;
        self.calculate_sums(self.input_list)
        self.calculate_epsilon();
        self.calculate_gamma();
        self.calculate_o2();
        self.calculate_co2();
    
    def calculate_o2(self):
        self.o2 = str('')
        filtered_list = self.input_list.copy()
        for each in range(len(self.input_list[0])):
            sums = self.calculate_sums(filtered_list)
            print(sums)
            if sums[each] >= len(filtered_list)/float(2):
                self.o2 += str(1);
            else: self.o2 += str(0);
            new_filtered_list = []
            for element in filtered_list:
                if element[each] == int(self.o2[-1]):
                    new_filtered_list.append(element)
            filtered_list = new_filtered_list

    def calculate_co2(self):
        self.co2 = str('')
        filtered_list = self.input_list.copy()
        for each in range(len(self.input_list[0])):
            sums = self.calculate_sums(filtered_list)
            if len(filtered_list) == 1:
                self.co2 = str('')
                for each in filtered_list[0]:
                    self.co2 += str(each);
                return
            if sums[each] < len(filtered_list)/float(2):
                self.co2 += str(1);
            else: self.co2 += str(0);
            new_filtered_list = []
            for element in filtered_list:
                if element[each] == int(self.co2[-1]):
                    new_filtered_list.append(element)
            filtered_list = new_filtered_list


    
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

    def calculate_sums(self,input_list):
        self.sums = [];
        for each in range(len(input_list[0])):
            self.sums.append(sum(i[each] for i in input_list))
        return self.sums

    def print_result(self):
        print('Gamma: '+self.gamma+'\n'+'Epsilon: '+self.epsilon)
        print('Gamma in decimal: ', int(int(self.gamma, 2)))
        print('Epsilon in decimal: ', int(int(self.epsilon, 2)))
        print('Gamma x Epsilon = ', int(self.gamma, 2) * int(self.epsilon, 2))
        print(self.o2, self.co2)
        print(int(self.o2, 2) * int(self.co2, 2))
