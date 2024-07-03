import pandas as pd
import numpy as np


class Calculator():
    def get_field(self):

        width = self.df.apply(
            lambda row:  row['x'] + row['width'], axis=1).max()

        height = self.df.apply(
            lambda row:  row['y'] + row['height'], axis=1).max()

        field = np.zeros((width, height))

        return field

    def update_field_with_next_row(self, row):
        for i in range(row['x'], row['x'] + row['width']):
            for j in range(row['y'], row['y'] + row['height']):
                print(row[0], i, j)

                self.field[i][j] += 1

    def __init__(self, df):
        self.df = df

    def calculate1(self):
        self.field = self.get_field()
        self.df.apply(self.update_field_with_next_row, axis=1)

        result = 0

        for row in self.field:
            for each in row:
                if each > 1:
                    result += 1
        return result

    def calculate2(self):
        pass
