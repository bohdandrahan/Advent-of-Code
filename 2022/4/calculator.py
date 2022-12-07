
class Calculator():
    def __init__(self, data_list):
        self.data = data_list;

    def isFullOverlap(self, pair):
        print(pair)
        if((pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])
            or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])):
            print(True)
            return True

        print(False)

        return False

    def isPartialOverlap(self, pair):
        print(pair)
        if((pair[0][0] <= pair[1][0] <= pair[0][1])
            or (pair[0][0] <= pair[1][1] <= pair[0][1])
            or (pair[1][0] <= pair[0][0] <= pair[1][1])
            or (pair[1][0] <= pair[0][1] <= pair[1][1])):
            print(True)
            return True

        print(False)

        return False

    def calculate1(self):
        result = 0
        for pair in self.data:
            if self.isFullOverlap(pair):
                result += 1

        return result

    def calculate2(self):
        result = 0
        for pair in self.data:
            if self.isPartialOverlap(pair):
                result += 1

        return result
