
class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        i = 0
        if len(self.data) > 13:
            self.data[1] = 12
            self.data[2] = 2

        while self.data[i] != 99:
            # print(self.data, "\n")
            if self.data[i] == 1:
                self.data[self.data[i+3]] = self.data[self.data[i+2]] + self.data[self.data[i+1]]  
            elif self.data[i] == 2:
                self.data[self.data[i+3]] = self.data[self.data[i+2]] * self.data[self.data[i+1]]  
            i += 4

        print(self.data, "end result \n")
        
        return self.data[0]

    def calculate2(self):
        for x in range(min(100, len(self.data))):
            for y in range(min(100, len(self.data))):
                print(len(self.data), "len")
                i = 0

                self.data[1] = x
                self.data[2] = y

                while self.data[i] != 99:
                    print(i, x,y ,"\n")
                    if(i+3 >= len(self.data)):
                        break
                    if self.data[i] == 1:
                        if (self.data[i+3] >= len(self.data)):
                            break
                        self.data[self.data[i+3]] = self.data[self.data[i+2]] + self.data[self.data[i+1]]  
                    elif self.data[i] == 2:
                        if (self.data[i+3] >= len(self.data)):
                            break
                        self.data[self.data[i+3]] = self.data[self.data[i+2]] * self.data[self.data[i+1]]  
                    i += 4  
                print(self.data)
                if self.data[0] == 19690720 :
                    return 100*x + y
        return -1
