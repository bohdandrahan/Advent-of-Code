import pandas as pd


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        self.df = pd.read_csv(file_path, header=None, sep="N/A")
        self.df['index', 'loc_x', 'loc_y', 'width', 'height'] = self.df[0].str.replace(
            r'#', '').replace(r'@', ',').replace(r":", ",").replace('x', ",").split(',')

    def get_data(self):
        print(self.df.head())
        return self.df

        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
