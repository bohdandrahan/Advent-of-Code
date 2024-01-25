
class Calculator():
    def __init__(self, data_list):
        self.data = data_list

    def calculate(self, data):
        pass

    def calculate1(self):
        s = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if ((x == 0 or self.data[y][x-1] not in "1234567890")
                    and self.data[y][x] in "1234567890"): #begining of the number
                    number = ""
                    x1 = x
                    while x1 != len(self.data[0]) and self.data[y][x1] in "1234567890":
                        number += self.data[y][x1]
                        x1 += 1
                    print("NUMBER", number)
                    if self.is_part_number(x, y, x1, number):
                        s += int(number)
        return s


    def is_part_number(self,x,y,x1,number):

        for i in range(x-1, x1+1):
            for j in range(-1, 2):
                if i < 0 or i >= len(self.data[0]):
                    continue
                if y+j < 0 or y+j >= len(self.data):
                    continue
                # print(j, i, self.data[y+j][i])
                if self.data[y+j][i] not in "1234567890.":
                    # print(number, "TRUE")
                    return True
        # print(number, "FALSE")
        return False

    def is_star_number(self,x,y,x1,number):
        print(x,y,x1)
        for i in range(x-1, x1+1):
            for j in range(-1, 2):
                if i < 0 or i >= len(self.data[0]):
                    continue
                if y+j < 0 or y+j >= len(self.data):
                    continue
                # print(j, i, self.data[y+j][i])
                if self.data[y+j][i] == "*":
                    return (y+j, i)

        return False
        
    def calculate2(self):
        result = 0
        stars = dict() 
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if ((x == 0 or self.data[y][x-1] not in "1234567890")
                    and self.data[y][x] in "1234567890"): #begining of the number
                    number = ""
                    x1 = x
                    while x1 != len(self.data[0]) and self.data[y][x1] in "1234567890":
                        number += self.data[y][x1]
                        x1 += 1
                    print("NUMBER", number)
                    star =  self.is_star_number(x, y, x1, number)
                    if star:
                        print('is_star!', star)
                        if star in stars:
                            stars[star].append(number)
                        else:
                            stars[star] = [number]
                        
        print(stars)
        for key, value in stars.items():
            if len(value) == 2:
                gear_ratio = int(value[0])*int(value[1])
                print(value, gear_ratio, 'gear')
                result += gear_ratio
        return result




