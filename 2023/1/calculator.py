
class Calculator():
    def __init__(self, data_list):
        self.data = data_list

    def calculate(self, data):
        pass

    def calculate1(self):
        sum = 0
        for each in self.data:
            start = ""
            end = ""

            for char in each:

                if char in "0123456789":
                    if start == "":
                        start = char
                    end = char

            number = int(start+end)
            sum += number
        return sum

    def calculate2(self):
        sum = 0
        spellings = ['this_number_is_here_to_be_instead_of_zero', 'one',
                     'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

        for each in self.data:
            start = ""
            end = ""

            for i, char in enumerate(each):

                if char in "0123456789":
                    if start == "":
                        start = char
                    end = char

                for j, number in enumerate(spellings):

                    # I'm very impressed that this worked the first time I ran it. I'm sure there are better solutions, but I'm quite impressed with myself
                    if each[i:len(number)+i] == number:
                        if start == "":
                            start = str(j)
                        end = str(j)

            number = int(start+end)
            sum += number
        return sum
