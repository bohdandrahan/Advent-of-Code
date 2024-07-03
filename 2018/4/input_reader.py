import pandas as pd


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        # 1 @ 249,597: 20x15

        self.df = pd.read_csv(file_path, header=None, sep=" ")

        self.df[['x', 'y']] = self.df[2].str.strip(r":") \
            .str.split(',', expand=True)

        self.df[['width', 'height']] = self.df[3].str.split('x', expand=True)

        self.df = self.df[[0, 'x', 'y', 'width', 'height']]

    def get_data(self):
        print(self.df.head())
        return self.df
