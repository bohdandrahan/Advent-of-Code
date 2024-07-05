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

                self.field[i][j] += 1

    def is_overlapping(self, rect1, rect2):

        return not (rect1['x'] + rect1['width'] <= rect2['x'] or
                    rect2['x'] + rect2['width'] <= rect1['x'] or
                    rect1['y'] + rect1['height'] <= rect2['y'] or
                    rect2['y'] + rect2['height'] <= rect1['y'])

    def check_if_not_overlapping(self, row):

        for i in range(len(self.df)):
            if i+1 == int(row[0][1:]):
                continue

            if self.is_overlapping(row, self.df.iloc[i]):
                return -1

        return int(row[0][1:])

    def __init__(self, df):
        self.df = df

    def calculate1(self):
        self.field = self.get_field()
        self.df.apply(self.update_field_with_next_row, axis=1)
        result = np.sum(self.field > 1)
        return result

    def calculate2(self):

        return self.df.apply(self.check_if_not_overlapping, axis=1).max()
