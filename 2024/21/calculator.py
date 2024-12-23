class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        self.pr(data)

        self.number_pad = [[7, 8, 9],
                           [4, 5, 6],
                           [1, 2, 3],
                           ["", 0, "A"]]

        self.number_pad_coords = dict()
        for x in range(len(self.number_pad)):
            for y in range(len(self.number_pad[0])):
                button = self.number_pad[x][y]
                self.number_pad_coords[button] = [x, y]

        self.pr(self.number_pad_coords)

        # Here is some cool one liner. it is not readable but it is very cool that you can actually do it.
        # self.number_pad_coords = {self.number_pad[x][y]: [x, y] for y in range(
        #     len(self.number_pad_coords[x])) for x in range(len(self.number_pad))}
        #
        # self.pr(self.number_pad_coords)

        self.directional_pad = [["", r"^", "A"],
                                [r"<", "v", r">"]]

        self.directional_pad_coords = dict()
        for x in range(len(self.directional_pad)):

            for y in range(len(self.directional_pad[0])):
                button = self.directional_pad[x][y]
                self.directional_pad_coords[button] = [x, y]
                self.pr("I can see this")

        self.pr(self.directional_pad_coords)

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):

        print('calculate 1 is running')

        return

    def calculate2(self):
        print('calculate 2 is running')

        return
