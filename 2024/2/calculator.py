class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        print('calculate 1 is running')
        sum = 0

        for each in self.data:
            if self.is_safe(each):
                sum += 1

        return sum

    def calculate2(self):
        print('calculate 2 is running')

        sum = 0

        for row in self.data:
            is_safe = False
            for i in range(len(row)):
                current = row[:i] + row[i+1:]
                if self.is_safe(current):
                    is_safe = True
                    break
            if is_safe:
                sum += 1

        return sum

    def is_safe(self, row):
        is_safe = True

        for i, each in enumerate(row):
            if i >= len(row)-1:
                break
            diff = row[i+1] - each

            if abs(diff) > 3 or abs(diff) < 1:
                is_safe = False
                break

        is_positive = row[1]-row[0] > 0

        for i, each in enumerate(row):
            if i >= len(row)-1:
                break

            diff = row[i+1] - each
            if (diff > 0) != is_positive:
                is_safe = False
                pass

        return is_safe
