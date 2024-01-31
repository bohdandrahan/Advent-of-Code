
class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        self.data.sort()
        
        left = 0
        right = len(self.data)-1

        while left != right:
            if self.data[left] + self.data[right] > 2020:
                right -=1
            elif self.data[left] + self.data[right] < 2020:
                left += 1
            else:
                print(self.data[right], self.data[left], self.data[right]+ self.data[left])
                return self.data[right]*self.data[left]
        
        return -1 #I don't think I need it, but just in case


    def calculate2(self):
        self.data.sort()
        

        for first in range(len(self.data)-2):
            left = first + 1 
            right = len(self.data)-1
            while left != right:
                if self.data[first] + self.data[left] + self.data[right] > 2020:
                    right -=1
                elif self.data[first] + self.data[left] + self.data[right] < 2020:
                    left += 1
                else:
                    return self.data[first]*self.data[right]*self.data[left]
        
        return -1 #I don't think I need it, but just in case
