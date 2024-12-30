from types import new_class


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
        return
