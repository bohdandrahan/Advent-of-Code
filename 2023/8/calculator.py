import math


class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        steps = 0
        i = 0
        current = 'AAA'
        while True:
            if current == 'ZZZ':
                break
            steps += 1
            rule = self.data['rules'][i % len(self.data['rules'])]
            if rule == 'R':
                current = self.data['nodes'][current][1]
            elif rule == 'L':
                current = self.data['nodes'][current][0]
            else:
                print('Something is wrong with rules')
                break
            # print(rule,current, self.data['nodes'][current])

            i += 1

        return steps

    def calculate2(self):
        currents = []
        all_steps = []

        for node in self.data['nodes']:
            if node[-1] == 'A':
                currents.append(node)

        for current in currents:
            i = 0
            steps = 0
            while True:
                if current[-1] == 'Z':
                    break
                steps += 1
                rule = self.data['rules'][i % len(self.data['rules'])]
                if rule == 'R':
                    current = self.data['nodes'][current][1]
                elif rule == 'L':
                    current = self.data['nodes'][current][0]
                else:
                    print('Something is wrong with rules')
                    break
                # print(rule,current, self.data['nodes'][current])

                i += 1

            all_steps.append(steps)

        return math.lcm(*all_steps)
