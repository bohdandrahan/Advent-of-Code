
class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        result = 0
        for each in self.data:
            result += each//3 - 2

        return result

    def calculate2(self):
        result = 0
        for each in self.data:
            while (each//3 - 2) > 0:

                result += each//3 - 2
                each = each//3-2

        return result
