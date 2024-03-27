

class Calculator():
    def __init__(self, data):
        self.data = data
        self.rotated_data = [self.rotate_data(each) for each in data]
        # print('START', self.rotated_data[0][0], len(
        #     self.rotated_data), 'ROTATED <---')
        # print('TEST', self.rotate_data(['123', '456', '789']))

    def rotate_data(self, matrix):
        matrix = [list(row) for row in matrix]

        transposed_matrix = list(zip(*matrix))

        rotated_matrix = ["".join(row[::-1]) for row in transposed_matrix]

        return rotated_matrix

    def calculate_box(self, box):
        for i, line in enumerate(box):
            # print(line)
            # print(i)
            possible_matches = []
            for j, each in enumerate(box[i + 1:], i+1):
                if each == line:
                    if (j - i) % 2 != 1:
                        continue

                    if not (i == 0 or j == len(box)-1):
                        continue

                    possible_matches.append(j)

            # if (len(possible_matches)) > 1:
                # print('MORE THAN ONE')

            for j in possible_matches:
                left = i
                right = j
                # print('possible match', j, i)

                mirror_match = True
                while right - left > 0:
                    if box[left] != box[right]:
                        mirror_match = False
                    right -= 1
                    left += 1
                    # print('curr left', left)

                if mirror_match:
                    return left

        return 0

    def calculate1(self):
        result = 0
        records = []
        for b, box in enumerate(self.rotated_data):
            result += self.calculate_box(box)
            if self.calculate_box(box) != 0:
                records.append(b)

        for b, box in enumerate(self.data):
            result += 100*self.calculate_box(box)

        return result

    def calculate2(self):
        pass
