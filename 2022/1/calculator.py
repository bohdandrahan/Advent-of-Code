
class Calculator():
    def __init__(self, data_list):
        self.data = data_list;

    def calculate(self, data):
        pass

    def calculate1(self):
        maxFood = 0
        for each in self.data:
            maxFood = max(maxFood, sum(each))
        return maxFood

    def calculate2(self):
        maxFood1 = maxFood2 = maxFood3 = 0
        for each in self.data:
            if maxFood1 < sum(each):
                maxFood2 = maxFood1
                maxFood1 = sum(each)
            else:
                if maxFood2 < sum(each):
                    maxFood3 = maxFood2
                    maxFood2 = sum(each)
                else:
                    if maxFood3 < sum(each):
                        maxFood3 = sum(each)
                        
        food = [maxFood1, maxFood2, maxFood3]
        print(food)
        return sum(food)
