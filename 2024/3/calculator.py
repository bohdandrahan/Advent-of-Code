class Calculator():
    def __init__(self, data):
        self.data: str = data
        self.left_number: int
        self.right_number: int
        self.go = True

    def calculate1(self):
        print('calculate 1 is running')
        mul_indexes = []
        start = 0
        while True:
            start = self.data.find("mul(", start)
            if start == -1:
                break
            mul_indexes.append(start)
            start += 1

        result = 0
        for i in mul_indexes:
            is_valid = self.validate(i)
            if is_valid:
                result += self.right_number * self.left_number

        return result

    def calculate2(self):
        print('calculate 1 is running')
        mul_indexes = []
        start = 0
        while True:
            start = self.data.find("mul(", start)
            if start == -1:
                break
            mul_indexes.append(start)
            start += 1

        do_indexes = []
        start = 0
        while True:
            start = self.data.find("do()", start)
            if start == -1:
                break
            do_indexes.append(start)
            start += 1

        dont_indexes = []
        start = 0
        while True:
            start = self.data.find("don't()", start)
            if start == -1:
                break
            dont_indexes.append(start)
            start += 1
        result = 0

        for i in range(len(self.data)):
            if i in do_indexes:
                self.go = True
            if i in dont_indexes:
                self.go = False
            if i in mul_indexes and self.go:
                is_valid = self.validate(i)
                if is_valid:
                    result += self.right_number * self.left_number

        return result

    def validate(self, index):
        self.left_number_str: str = ""
        self.right_number_str: str = ""
        is_valid = True

        has_seen_coma = False

        index += 4
        while is_valid:
            if index > len(self.data):
                is_valid = False
                break
            if self.data[index].isdigit():
                if not has_seen_coma:
                    self.left_number_str += str(self.data[index])
                else:
                    self.right_number_str += str(self.data[index])

                index += 1
                continue
            elif self.data[index] == "," and not has_seen_coma:
                has_seen_coma = True
                index += 1
                continue
            elif self.data[index] == ")" and has_seen_coma:
                break

            else:
                is_valid = False
                break
        if is_valid:
            if self.left_number_str == "" or self.right_number_str == "":
                is_valid = False
            else:
                self.left_number = int(self.left_number_str)
                self.right_number = int(self.right_number_str)

        return is_valid
