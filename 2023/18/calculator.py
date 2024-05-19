
class Calculator():
    def __init__(self, data):
        self.data = data
        self.directions = {"U": (-1, 0), "R": (0, 1),
                           "D": (1, 0), "L": (0, -1)}

    def get_coordinates(self):
        current = (0, 0)
        self.coords = [current]

        for each in self.data:
            next = self.directions[each[0]]

            current = (current[0] + next[0]*each[1],
                       current[1]+next[1]*each[1])
            self.coords.append(current)

        return self.coords

    def get_polygon_area(self):
        self.get_coordinates()
        # self.coords = self.coords[:-1]
        perimeter = 0
        for each in self.data:
            perimeter += each[1]
        print(perimeter/2)

        area = 0
        j = len(self.coords) - 1

        for i in range(len(self.coords)):
            area += (self.coords[j][0] + self.coords[i][0]) * \
                (self.coords[j][1] - self.coords[i][1])
            j = i

        return area / 2 + perimeter/2+1

    def calculate1(self):
        return self.get_polygon_area()

    def calculate2(self):
        pass
