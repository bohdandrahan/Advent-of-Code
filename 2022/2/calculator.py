
class Calculator():
    def __init__(self, data_list):
        self.data = data_list;


    def calculate(self, data):
        pass

    def calculate1(self):

        self.ScoreMap = {};
        self.ScoreMap["A"] = {"X": 3, "Y":  6, "Z": 0 }
        self.ScoreMap["B"] = {"X": 0, "Y":  3, "Z": 6 }
        self.ScoreMap["C"] = {"X": 6, "Y":  0, "Z": 3 }

        score = 0
        for each in self.data:
            if each[1] == "X":
                score += 1
            elif each[1] == "Y":
                score += 2
            elif each[1] == "Z":
                score += 3

            score += self.ScoreMap[each[0]][each[1]]

        return score


    def calculate2(self):

        self.ScoreMap = {};
        self.ScoreMap["A"] = {"X": 3, "Y":  4, "Z": 8 }
        self.ScoreMap["B"] = {"X": 1, "Y":  5, "Z": 9 }
        self.ScoreMap["C"] = {"X": 2, "Y":  6, "Z": 7 }

        score = 0
        for each in self.data:
            score += self.ScoreMap[each[0]][each[1]]

        return score
