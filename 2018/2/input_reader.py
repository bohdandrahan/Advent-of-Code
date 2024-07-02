import pandas as pd


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        self.data = pd.read_csv(file_path, header=None)

    def get_data(self):
        return self.data

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
