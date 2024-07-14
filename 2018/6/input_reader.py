import pandas as pd


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        self.df = pd.read_csv(file_path, names=['x', 'y'])

    def get_data(self):
        pd.set_option('display.max_columns', None)
        print(self.df.head(5))
        return self.df
