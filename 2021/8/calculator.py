
class Calculator():
    def __init__(self, data):
        self.data = data
        self.chars = ["a","b","c","d","e","f","g"]


        self.solve_part_1()
        self.solve_part_2()

    def solve_part_1(self):
        self.total = 0
        for each in self.data.values():
            for seven_segment_digit in each:
                l = len(seven_segment_digit)
                if (l == 2 or l==3 or l== 4 or l== 7):
                    self.total += 1
        print("Part 1 Total:", self.total)

    def solve_part_2(self):
        self.total = 0

        for unique_digits, output_digits in self.data.items():
            self.total += self.calculate_row(unique_digits, output_digits)

        print("Part 2 Total:", self.total)


    def calculate_row(self, unique_digits, output_digits):

        all_chars = self.get_all_chars(unique_digits)

        map = self.decode(all_chars, unique_digits)

        row_num = ''
        for digit in output_digits:
            for num, code in map.items():
                if set(digit) == set(code):
                    row_num += str(num)

        return int(row_num)

    def get_all_chars(self, unique_digits):
        all_chars = {self.chars[i]: 0 for i, char in enumerate(self.chars)}
        for digit in unique_digits:
            for char in digit:
                all_chars[char] += 1
        return all_chars

    def decode(self, all_chars, unique_digits):
        decoder = {}

        map = {}
        for digit in unique_digits:
            if len(digit) == 2:
                map[1] = digit
            if len(digit) == 3:
                map[7] = digit
            if len(digit) == 4:
                map[4] = digit
            if len(digit) == 7:
                map[8] = digit

        for i in map[7]:
            if i not in map[1]:
                decoder['a'] = i

        for char, qty in all_chars.items():
            if qty == 4:
                decoder['e'] = char
            if qty == 6:
                decoder['b'] = char
            if qty == 9:
                decoder['f'] = char
            if qty == 8:
                if char != decoder['a']:
                    decoder['c'] = char
        for i in map[4]:
            if i not in map[7] and i !=decoder['b']:
                decoder['d'] = i

        for char in self.chars:
            if char not in decoder.values():
                decoder['g'] = char

        for digit in unique_digits:
            if len(digit) == 6 and decoder['d'] not in digit:
                map[0] = digit
            if len(digit) == 6 and decoder['c'] not in digit:
                map[6] = digit
            if len(digit) == 6 and decoder['e'] not in digit:
                map[9] = digit

            if len(digit) == 5 and decoder['b'] not in digit and decoder['f'] not in digit:
                map[2] = digit
            if len(digit) == 5 and decoder['b'] not in digit and decoder['e'] not in digit:
                map[3] = digit
            if len(digit) == 5 and decoder['b'] in digit:
                map[5] = digit

        return map


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg
#

#           Notes:
# 2:1, 3:7, 4:4, 5:2,3,5, 6:6,9,0, 7:8
# 8:A,C, 9:F, 7:D,G 6:B, 4:E,
#
# a = in 1 not in 7 -- A,F,B,E 1,4,7,8
# C and A both 8 times - A, B, C, F, E
# D in 4 not in 7 and B is known - A, B, C, D, E, F
# the leftover is G
#
