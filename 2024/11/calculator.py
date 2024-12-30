from typing import DefaultDict


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

        stones = list(self.data)

        for i in range(25):
            new_stones = list()

            for stone in stones:
                if stone == 0:
                    new_stones.append(1)
                elif len(str(stone)) % 2 == 0:
                    self.pr(len(str(stone))//2)
                    new_stones.append(int(str(stone)[:len(str(stone))//2]))

                    new_stones.append(int(str(stone)[len(str(stone))//2:]))
                else:
                    new_stones.append(stone * 2024)
            stones = new_stones

        return len(stones)

    def calculate2(self):
        print('calculate 2 is running')

        stones = list(self.data)
        stones_count = DefaultDict(int)
        for stone in stones:
            stones_count[stone] += 1

        for i in range(75):
            self.pr("BLINK NUMBER ", i)

            new_stones = DefaultDict(int)

            for stone in stones_count:
                if stone == 0:
                    new_stones[1] += stones_count[0]
                elif len(str(stone)) % 2 == 0:
                    new_stones[int(str(stone)[:len(str(stone))//2])
                               ] += stones_count[stone]
                    new_stones[int(str(stone)[len(str(stone))//2:])
                               ] += stones_count[stone]
                else:
                    new_stones[stone * 2024] += stones_count[stone]
            stones_count = new_stones

        return sum(stones_count.values())
