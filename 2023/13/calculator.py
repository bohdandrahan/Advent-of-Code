
import enum
import sre_constants


class Calculator():
    def __init__(self, data):
        self.data = data

    def count_row(self, row):
        print('count_row', row)
        count = 0

        def dfs(string):
            nonlocal count

            if '?' not in string:
                record = []
                prev = '.'
                for char in string:
                    if char == '#' and prev == '.':
                        record.append(1)
                    elif char == '#' and prev == '#':

                        record[-1] += 1
                    prev = char

                # print(string, record, row[1])

                if record == row[1]:
                    count += 1

            else:
                if not self.check_if_possible(string, row):
                    return 0

                i = string.index('?')
                stirng = string[:i] + '.' + string[i+1:]
                dfs(stirng)

                string = string[:i] + '#' + string[i+1:]
                dfs(string)

        dfs(row[0])

        return count

    def check_if_possible(self, string, row):

        i = string.index('?')

        record = []
        prev = '.'
        for char in string[:i]:
            if char == '#' and prev == '.':
                record.append(1)
            elif char == '#' and prev == '#':

                record[-1] += 1
            prev = char

        # print(string, record, row[1])

        for j, each in enumerate(record):

            if j == len(record)-1:
                break
            if j < len(row[1]) and each != row[1][j]:
                return False

        return True

    def calculate1(self):
        count = 0

        for each in self.data:
            count += self.count_row(each)

        return count

    def calculate2(self):

        count = 0

        expanded_data = list(self.data)

        for i, each in enumerate(expanded_data):
            print('ROW', i)
            each[0] = each[0]*5
            each[1] = each[1]*5

            count += self.count_row(each)

        return count
