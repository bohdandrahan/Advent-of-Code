class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        self.pr(data)

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):

        print('calculate 1 is running')

        result = 0
        for secret_number in self.data:
            current_secret_number = secret_number

            for i in range(2000):
                # Calculate the result of multiplying the secret number by 64.
                # Then, mix this result into the secret number. Finally, prune the secret number.
                current_secret_number = (
                    current_secret_number * 64) ^ current_secret_number
                current_secret_number = current_secret_number % 16777216
                # Calculate the result of dividing the secret number by 32.
                # Round the result down to the nearest integer. Then, mix this result into the secret number.
                # Finally, prune the secret number.
                current_secret_number = (
                    current_secret_number // 32) ^ current_secret_number
                current_secret_number = current_secret_number % 16777216

                # Calculate the result of multiplying the secret number by 2048.
                # Then, mix this result into the secret number.
                # Finally, prune the secret number.

                current_secret_number = (
                    current_secret_number * 2048) ^ current_secret_number

                current_secret_number = current_secret_number % 16777216
                self.pr(secret_number, current_secret_number)

            result += current_secret_number

        return result

    def calculate2(self):
        print('calculate 2 is running')

        result = 0

        top_seq_count = {}
        for secret_number in self.data:
            current_secret_number = secret_number

            seen_top_seq = dict()

            seq = [int(str(secret_number)[-1])]
            seq_diff = []

            for i in range(2000):
                # Calculate the result of multiplying the secret number by 64.
                # Then, mix this result into the secret number. Finally, prune the secret number.
                current_secret_number = (
                    current_secret_number * 64) ^ current_secret_number
                current_secret_number = current_secret_number % 16777216
                # Calculate the result of dividing the secret number by 32.
                # Round the result down to the nearest integer. Then, mix this result into the secret number.
                # Finally, prune the secret number.
                current_secret_number = (
                    current_secret_number // 32) ^ current_secret_number
                current_secret_number = current_secret_number % 16777216

                # Calculate the result of multiplying the secret number by 2048.
                # Then, mix this result into the secret number.
                # Finally, prune the secret number.

                current_secret_number = (
                    current_secret_number * 2048) ^ current_secret_number

                current_secret_number = current_secret_number % 16777216
                seq.append(int(str(current_secret_number)[-1]))

                if len(seq) == 1:
                    seq_diff.append(seq[-1])
                else:
                    seq_diff.append(seq[-1]-seq[-2])

                if len(seq_diff) >= 4:
                    last_4 = tuple(seq_diff[-4:])
                    if last_4 in seen_top_seq:
                        continue
                    else:
                        seen_top_seq[last_4] = seq[-1]

            # self.pr(top_seq_count)
            self.pr(seq_diff, secret_number)
            self.pr(seq, secret_number)

            for each_seen in seen_top_seq:
                if each_seen in top_seq_count:
                    top_seq_count[each_seen] += seen_top_seq[each_seen]
                else:
                    top_seq_count[each_seen] = seen_top_seq[each_seen]

        max_result = 0
        top_4 = tuple([0, 0, 0, 0])
        for each in top_seq_count:
            max_result = max(top_seq_count[each], max_result)
            top_4 = each
            if top_seq_count[each] == 23:
                self.pr(23, "THIS IS IT", each)

        self.pr(top_4)
        self.pr(top_seq_count[tuple([-2, 1, -1, 3])])

        return max_result
