class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        print('calculate 1 is running')

        result = 0

        for row in self.data:
            if self.do_the_thing(row[0], row[1][0], row[1][1:]):
                result += row[0]

        return result  # time to solve 22m:25s

    def calculate2(self):
        print('calculate 2 is running')

        result = 0

        for row in self.data:
            if self.do_the_thing(row[0], row[1][0], row[1][1:], is_concat=True):
                result += row[0]

        return result  # time to solve 2h:11m44s

    def do_the_thing(self, goal, current, numbers_left, is_concat=False):
        if len(numbers_left) == 0:
            return goal == current
        result = self.do_the_thing(goal, current * numbers_left[0], numbers_left[1:], True) \
            or self.do_the_thing(goal, current + numbers_left[0], numbers_left[1:], True)
        if is_concat:
            result = result or self.do_the_thing(
                goal, int(str(current) + str(numbers_left[0])), numbers_left[1:], True)
        return result
