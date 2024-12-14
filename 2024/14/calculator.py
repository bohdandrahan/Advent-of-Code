class Calculator():
    def __init__(self, data):
        self.data = data
        self.is_test = data["is_test"]

        # convention from here and now-on:
        # X is index by widht
        # Y is index by height.
        # I know, it's just a bit unintuitive but because we itterate
        # over rows first then over each element, X is logically associated with rows and not columns.:

        self.width = 11 if data["is_test"] else 101
        self.height = 7 if data["is_test"] else 103

        self.number_of_seconds_to_run = 100
        self.quadrant_ranges_x = [[0, self.width//2],
                                  [self.width//2 + 1, self.width]]
        self.quadrant_ranges_y = [[0, self.height//2],
                                  [self.height//2 + 1, self.height]]

    def calculate1(self):
        print('calculate 1 is running')
        self.finished_map = [[0 for y in range(self.height)]
                             for x in range(self.width)]
        for robot in self.data["robots"]:
            finish_position = self.get_position_after_N_seconds(
                robot["position"], robot["velocity"], self.number_of_seconds_to_run)

            self.finished_map[finish_position[0]][finish_position[1]] += 1

        result = 1
        for quadrant_x in self.quadrant_ranges_x:
            for quadrant_y in self.quadrant_ranges_y:
                current_num = 0
                for x in range(quadrant_x[0], quadrant_x[1]):
                    for y in range(quadrant_y[0], quadrant_y[1]):
                        current_num += self.finished_map[x][y]
                result *= current_num
        return result

    def calculate2(self):
        print('calculate 2 is running')
        return

    def get_position_after_N_seconds(self, position, velocity, N):
        next_position = [position[0] + velocity[0], position[1] + velocity[1]]
        next_position = [next_position[0] % self.width,
                         next_position[1] % self.height]
        if N == 1:
            return next_position
        else:
            return self.get_position_after_N_seconds(next_position, velocity, N - 1)
