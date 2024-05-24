
class Calculator():
    def __init__(self, data):
        self.data = data
        self.directions = {"U": (-1, 0), "R": (0, 1),
                           "D": (1, 0), "L": (0, -1)}
        self.directions_hex = {0: "R", 1: "D", 2: "L", 3: "U"}

    def get_data_hex(self):
        data_hex = []
        for each in self.data:
            dir = self.directions_hex[int(each[2][-2])]
            steps = int(each[2][2:-2], 16)
            data_hex.append([dir, steps])
        self.data_hex = data_hex
        return data_hex

    def get_coordinates(self, data):
        current = (0, 0)
        self.coords = [current]

        for each in data:
            next = self.directions[each[0]]

            current = (current[0] + next[0]*each[1],
                       current[1]+next[1]*each[1])
            self.coords.append(current)

        return self.coords

    def get_polygon_area(self, coords, data):
        perimeter = 0
        for each in data:
            perimeter += each[1]

        area = 0
        j = len(coords) - 1

        for i in range(len(coords)):
            area += (coords[j][0] + coords[i][0]) * \
                (coords[j][1] - coords[i][1])
            j = i

        # shoelace formula but with added petimeter because we have a "stroke" of the len 1
        # I'm not sure why I need to add 1 in the end excactly, but probably because in the end of the polygon it will be turned 4 time with a small quarter of the square without accounting all of the turns that will cancel them out
        # I'm happy with the fact that I have this intuition and the algorythm works

        return area / 2 + perimeter/2+1

    def calculate1(self):
        self.get_coordinates(self.data)
        return self.get_polygon_area(self.coords, self.data)

    def calculate2(self):
        self.get_data_hex()
        self.get_coordinates(self.data_hex)
        return self.get_polygon_area(self.coords, self.data_hex)
