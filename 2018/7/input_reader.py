import pandas as pd


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        with open(file_path) as file:
            lines = file.readlines()

        pairs = []
        for line in lines:
            parent = line[5]
            child = line[36]
            pairs.append([parent, child])

        self.df = pd.DataFrame(pairs, columns=["paretn", "child"])

    def get_data(self):
        pd.set_option('display.max_columns', None)
        print(self.df.head(5))
        return self.df
