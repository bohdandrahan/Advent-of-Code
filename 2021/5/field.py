import numpy as np


class Field():
    def __init__(self):
        self.field = np.empty((999,999), int)

    
    def add_lines(self, lines):
        for each in lines:
            self.add_line(each)

    def add_line(self, line):
        for point in line.get_points():
            self.field[point[0], point[1]] += 1
    
    def calculate_number_of_overlaping_points(self):
        self.number_of_overlaping_points = 0
        for ix, iy in np.ndindex(self.field.shape):
            if self.field[ix, iy] > 1:
                self.number_of_overlaping_points += 1

    def get_number_of_overlaping_points(self):
        return self.number_of_overlaping_points