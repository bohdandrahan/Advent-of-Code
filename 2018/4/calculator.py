from time import sleep
import pandas as pd


def update_minutes_slept(row, table):
    for i in range(row['time_start_sleep'], row['time_end_sleep']):
        table[i] += 1


class Calculator():
    def __init__(self, df):
        self.df = df

    def calculate_sleep_sessions(self):
        sleep_sessions = pd.DataFrame([], columns=['guard_id', 'day',
                                                   'time_start_sleep', 'time_end_sleep',
                                                   'duration'])

        current_guard = None
        current_day = None
        current_time_start = None
        for index, row in self.df.iterrows():
            if row['event'][:5] == 'Guard':

                current_guard = int(row['event'].split(" ")[1][1:])

                # in case the guard went on his shift the day earlier
                day = row['day'] if (row['hour']) == 0 else row['day'] + 1

                current_day = '{0}-{1}-{2}'.format(
                    row['year'], row['month'], day)

            if row['event'] == 'falls asleep':
                if current_day == None or current_guard == None:
                    raise Exception(
                        "Something is worng, we should have day or gguard at this moment")

                current_time_start = row['minute']

            if row['event'] == 'wakes up':

                if current_time_start == None or current_day == None or current_guard == None:
                    raise Exception(
                        "Something is worng, we should have day or guard or start time at this moment")

                current_time_end = row['minute']
                duration = current_time_end - current_time_start

                sleep_sessions.loc[len(sleep_sessions)] = {'guard_id': current_guard,
                                                           'day': current_day,
                                                           'time_start_sleep': current_time_start,
                                                           'time_end_sleep': current_time_end,
                                                           'duration': duration}

                current_time_start == None
        self.sleep_sessions = sleep_sessions

    def calculate1(self):
        self.calculate_sleep_sessions()
        most_slept_guard = self.sleep_sessions.groupby(
            ['guard_id'])['duration'].sum().idxmax()

        minutes_slept = pd.Series(0, index=range(60))

        self.sleep_sessions.query(
            'guard_id == @most_slept_guard').apply(update_minutes_slept, args=[minutes_slept], axis=1)
        most_slept_minute = minutes_slept.idxmax()
        return most_slept_guard * most_slept_minute

    def calculate2(self):

        self.calculate_sleep_sessions()

        max_value_slept_min = 0
        max_slept_min = None
        max_guard = None

        for guard in self.sleep_sessions['guard_id'].unique():
            print('GUARD', guard)

            minutes_slept = pd.Series(0, index=range(60))

            self.sleep_sessions.query(
                'guard_id == @guard').apply(update_minutes_slept, args=[minutes_slept], axis=1)

            most_slept_minute = minutes_slept.idxmax()

            if minutes_slept[most_slept_minute] > max_value_slept_min:
                max_value_slept_min = minutes_slept[most_slept_minute]
                max_slept_min = most_slept_minute
                max_guard = guard

        return max_guard * max_slept_min
