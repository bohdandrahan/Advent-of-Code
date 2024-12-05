class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        print('calculate 1 is running')

        sum = 0
        for update in self.data[1]:
            if self.get_is_correct_update(update):
                sum += self.get_middle_number(update)

        return sum

        # 30m:12.64s to finish firts star

    def calculate2(self):
        print('calculate 2 is running')

        sum = 0
        for update in self.data[1]:
            if not self.get_is_correct_update(update):
                self.fix_update(update)
                sum += self.get_middle_number(update)

        return sum

    def fix_update(self, update):
        for j in range(100):
            for rule in self.data[0]:
                if rule[0] not in update or rule[1] not in update:
                    continue

                if update.index(rule[0]) > update.index(rule[1]):
                    temp = update[update.index(rule[0])]
                    update[update.index(
                        rule[0])] = update[update.index(rule[1])]
                    update[update.index(rule[1])] = temp

    def get_is_correct_update(self, update):
        is_correct = True
        for rule in self.data[0]:
            if rule[0] not in update or rule[1] not in update:
                continue
            if update.index(rule[0]) > update.index(rule[1]):
                is_correct = False
                break

        return is_correct

    def get_middle_number(self, update):
        return update[len(update)//2]
