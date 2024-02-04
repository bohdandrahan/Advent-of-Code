
class Calculator():
    def __init__(self, data):
        #0-min 1-max 2-char 3 password
        self.data = data
        

    def calculate1(self):
        valid_count = 0
        for each in self.data:
            if each[0] <= each[3].count(each[2]) <= each[1]:
                valid_count += 1
        return valid_count

    def calculate2(self):
        valid_count = 0
        for each in self.data:
            if bool(each[3][each[0]-1] == each[2]) ^ bool(each[3][each[1]-1] == each[2]):
                valid_count +=  1

        return valid_count
