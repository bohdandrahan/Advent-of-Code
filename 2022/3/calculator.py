
class Calculator():
    def __init__(self, data_list):
        self.data = data_list;

#91>char -> lowercase

    def calculate(self, data):
        pass

    def calculate1(self):
        points = 0
        for each in self.data:
            oddChar = list(set(each[0]) & set(each[1]))[0]
            points += self.calculatePoints(oddChar)
        return points

    def calculate2(self):
        groups = {}
        for i, each in enumerate(self.data):
            print(i, i//3, i%3)
            if(i%3 ==0):
                groups[i//3] = {}
            groups[i//3][i%3] = each[0] + each[1]

        points = 0
        for key, value in groups.items():
            group = value
            oddChar = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            points += self.calculatePoints(oddChar)

        return points

    def calculatePoints(self,oddChar):
        if ord(oddChar) > 91:
            return ord(oddChar)-ord('a')+1
        else:
            return ord(oddChar)-ord('A')+27
