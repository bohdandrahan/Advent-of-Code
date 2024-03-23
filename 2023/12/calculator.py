
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
                i = string.index('?')
                stirng = string[:i] + '.' + string[i+1:]
                dfs(stirng)

                string = string[:i] + '#' + string[i+1:]
                dfs(string)

        dfs(row[0])

        return count

    def calculate1(self):
        count = 0

        for each in self.data:
            count += self.count_row(each)

        return count

    def calculate2(self):
        pass
