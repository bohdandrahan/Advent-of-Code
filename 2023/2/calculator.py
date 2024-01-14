
class Calculator():
    def __init__(self, data_list):
        self.data = data_list
        self.limit = {"red": 12, "green": 13, "blue": 14}

    def calculate(self, data):
        pass

    def calculate1(self):
        s = 0
        for i, game in enumerate(self.data):
            if self.is_valid_game(game):
                s += i + 1
        
        return s
        
    def calculate2(self):
        s = 0
        for i, game in enumerate(self.data):
            s += self.get_power(game)   
        return s

    def get_power(self, game):
        colors = [0,0,0]
        for set in game:
            updated_set = [element.strip().strip("\n") for element in set.split(",")]
            set = updated_set
            for pair in set:
                pair_data = pair.split(" ")

                if pair_data[1] == "red":
                    colors[0] = max(colors[0], int(pair_data[0]))
                if pair_data[1] == "green":
                    colors[1] = max(colors[1], int(pair_data[0]))
                if pair_data[1] == "blue":
                    colors[2] = max(colors[2], int(pair_data[0]))
        
        print(colors)
        
        return colors[0]*colors[1]*colors[2]
            

    def is_valid_game(self, game):
        is_valid = True

        for set in game:
            updated_set = [element.strip().strip("\n") for element in set.split(",")]
            set = updated_set
            for pair in set:
                pair_data = pair.split(" ")
                
                if self.limit[pair_data[1]] < int(pair_data[0]):
                    is_valid = False
        return is_valid