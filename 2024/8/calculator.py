from typing import Dict, List


class Calculator():

    def __init__(self, data):
        self.data = data

    def calculate1(self, is_part_2=False):
        print('calculate 1 is running')

        self.antidote_map = [[False for each in row] for row in self.data]

        self.anthenas: Dict[str, List[List[int]]]
        self.anthenas = {}
        self.already_checked_locations = set()

        for x, row in enumerate(self.data):
            for y, char in enumerate(row):
                if char != '.':
                    if char in self.anthenas:
                        self.anthenas[char].append([x, y])
                    else:
                        self.anthenas[char] = [[x, y]]
        for char, locations in self.anthenas.items():
            for i, location in enumerate(locations):
                next_i = i + 1
                while next_i < len(locations):
                    self.check_and_update_antidote_map(
                        location, locations[next_i], char, is_part_2)
                    next_i += 1

        print([[1 if each else 0 for each in row]
              for row in self.antidote_map])
        result = sum(sum(row) for row in self.antidote_map)

        # print(self.already_checked_locations)
        return result

    def calculate2(self):
        return self.calculate1(is_part_2=True)

    def check_and_update_antidote_map(self, location1, location2, char, is_part_2=False):
        if tuple(tuple(location1) + tuple(location2) + tuple([char])) in self.already_checked_locations:
            return
        else:
            self.already_checked_locations.add(
                tuple(tuple(location1) + tuple(location2) + tuple([char])))

        diff_vector = [location2[0] - location1[0],
                       location2[1] - location1[1]]

        antidote_locations = list()
        antidote_locations.append(
            [location2[0] + diff_vector[0], location2[1] + diff_vector[1]])
        antidote_locations.append(
            [location1[0] - diff_vector[0], location1[1] - diff_vector[1]])

        for location in antidote_locations:
            if location[0] >= 0 and location[0] < len(self.data) \
                    and location[1] >= 0 and location[1] < len(self.data[0]):
                print(len(self.data[0]), len(self.data))
                self.antidote_map[location[0]][location[1]] = True
                if is_part_2:
                    self.check_and_update_antidote_map(
                        location1, location, char, is_part_2)
                    self.check_and_update_antidote_map(
                        location2, location, char, is_part_2)
