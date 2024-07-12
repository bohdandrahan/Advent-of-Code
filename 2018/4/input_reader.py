from numpy import column_stack, full
import pandas as pd
from pandas._libs.tslibs import timestamps


class Input_Reader():
    def __init__(self, file_path):
        self.convert_to_df(file_path)

    def convert_to_df(self, file_path):

        # Input Example:
        # [1518-11-05 00:03] Guard #99 begins shift
        # [1518-11-05 00:45] falls asleep
        # [1518-11-05 00:55] wakes up

        file = open(file_path)
        data = file.readlines()
        file.close()

        parsed_data = []
        for each in data:

            timestamp, event = each.split(r"] ")

            timestamp = timestamp[1:]
            event = event.strip()

            parsed_data.append([timestamp, event])

        self.df = pd.DataFrame(parsed_data)
        self.df.columns = ['timestamp', 'event']

        self.df['year'] = self.df['timestamp'].apply(lambda x: x[0:4])
        self.df['month'] = self.df['timestamp'].apply(lambda x: x[5:7])
        self.df['day'] = self.df['timestamp'].apply(lambda x: x[8:10])
        self.df['hour'] = self.df['timestamp'].apply(lambda x: x[11:13])
        self.df['minute'] = self.df['timestamp'].apply(lambda x: x[14:16])

        self.df['year'] = self.df['year'].astype(int)
        self.df['month'] = self.df['month'].astype(int)
        self.df['day'] = self.df['day'].astype(int)
        self.df['hour'] = self.df['hour'].astype(int)
        self.df['minute'] = self.df['minute'].astype(int)

        self.df = self.df.sort_values(
            by=['year', 'month', 'day', 'hour', 'minute'], ascending=True)

    def get_data(self):
        pd.set_option('display.max_columns', None)
        print(self.df.head())
        return self.df
