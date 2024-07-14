import pandas as pd
import numpy as np


class Calculator():

    def __init__(self, df):
        self.df = df

    def generate_map(self):
        self.max_x = self.df['x'].max()
        self.max_y = self.df['y'].max()

        map = np.full((self.max_x + 1, self.max_y + 1), -1)
        self.map = map

    def get_distance(self, row, x, y):

        distance = int(abs(row['x'] - x) + abs(row['y'] - y))
        return distance

    def get_closest_points(self, x, y):
        distance_table = pd.DataFrame(self.df.apply(self.get_distance,
                                                    args=[x, y], axis=1))
        distance_table.columns = ['distance']

        min_distance = distance_table.min()

        points = distance_table[distance_table['distance']
                                == min_distance['distance']]
        return points

    def calculate1(self):
        self.generate_map()

        for index, element in np.ndenumerate(self.map):
            x = index[0]
            y = index[1]

            points = self.get_closest_points(x, y)

            if len(points) == 1:
                self.map[x][y] = points.index[0]

        infinite_points: set = set()
        for index, element in np.ndenumerate(self.map):
            x = index[0]
            y = index[1]
            if x == 0 or y == 0 or x == self.max_x or y == self.max_y:
                infinite_points.add(int(self.map[x][y]))

        points: set = set(range(len(self.df)))
        for each in infinite_points:
            if int(each) in points:
                points.remove(int(each))

        max_count = 0
        for point in points:
            count = 0
            for row in self.map:
                for each in row:
                    if each == point:
                        count += 1
            max_count = max(max_count, count)

        return max_count

    def calculate2(self):
        self.generate_map()

        for index, element in np.ndenumerate(self.map):
            x = index[0]
            y = index[1]

            distance_table = pd.DataFrame(self.df.apply(self.get_distance,
                                                        args=[x, y], axis=1))
            distance_table.columns = ['distance']

            self.map[x][y] = (distance_table['distance'].sum())

        count = 0
        for index, element in np.ndenumerate(self.map):
            x = index[0]
            y = index[1]

            if self.map[x][y] < 10000:
                count += 1

        return count
