
class Calculator():
    def __init__(self, data):
        self.data = data
        self.calculate_records()

    def calculate_records(self):
        records = []

        for each in self.data:
            records.append([each])
            curr = each
            end = False
            while not end:
                end = True
                new_curr = []
                for i in range(len(curr) - 1):
                    new_curr.append(curr[i+1] - curr[i])
                    if new_curr[-1] != 0:
                        end = False
                curr = new_curr
                records[-1].append(curr)

        self.records = records

    def calculate1(self):
        nums = []
        for record in self.records:
            next_number = 0

            i = len(record) - 1
            while i >= 0:
                next_number += record[i][-1]
                i -= 1

            nums.append(next_number)

        return sum(nums)

    def calculate2(self):
        nums = []
        for record in self.records:

            first_number = 0

            i = len(record) - 1
            while i > 0:
                first_number = record[i-1][0] - first_number
                i -= 1

            nums.append(first_number)

        return sum(nums)
