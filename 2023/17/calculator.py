import heapq


class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):
        maze = MazeSolver(self.data, 3, 1)
        return maze.calculate_path()

    def calculate2(self):
        maze = MazeSolver(self.data, 10, 4)
        return maze.calculate_path()


class MazeSolver():
    def __init__(self,
                 field,
                 single_direction_limit_max,
                 single_direction_limit_min):
        self.directions = {
            'up': [-1, 0], 'right': [0, 1], 'down': [1, 0], 'left': [0, -1]}
        self.curr_temp = 0
        self.curr_coord = (0, 0)
        self.prev_direction = 'left'
        self.prev_step_count = 0
        self.field = field
        self.single_direction_limit_max = single_direction_limit_max
        self.single_direction_limit_min = single_direction_limit_min
        self.finish_coord = (len(self.field)-1, len(self.field[0]) - 1)
        self.seen = set()  # format of seen is (curr_coord, prev_direcion, prev_steps, temp)
        self.path = dict()  # same format as seen, but with referense to another step

    def calculate_path(self):

        queue = [(0, (self.curr_coord, self.prev_direction,
                      self.prev_step_count, self.curr_temp))]

        end = (0, 1, 2, 3)
        i = 0
        while self.curr_coord != self.finish_coord and queue:
            # for i in range(10):
            curr = heapq.heappop(queue)
            curr = curr[1]
            self.curr_coord = curr[0]
            self.prev_direction = curr[1]
            self.prev_step_count = curr[2]
            self.curr_temp = curr[3]
            # print('CURR', curr)

            potential_next_steps = self.get_list_of_potential_next_steps()
            for each in potential_next_steps:
                heapq.heappush(queue, (each[-1], each))
                self.seen.add(each[:-1])
                self.path[each] = curr
            end = curr

            # if (i % 100000) == 0:
            #     print(i, curr)
            # i += 1

        end_path = [end[0]]
        while end[0] != (0, 0):
            end = self.path[end]
            end_path.append(end[0])

        # for i in self.field:
        #     print(i)
        solved = list(self.field)
        for i, line in enumerate(solved):
            for j, temperature in enumerate(line):
                solved[i] = list(line)
                line = list(line)
                if (i, j) in end_path:
                    line[j] = 0
                    # print(i, j, 'LOCATION')
                    # print(line)
                    solved[i] = line

        # print('\n')
        # for i in solved:
        #     print(i)
        # print(self.curr_temp)
        return self.curr_temp

    def get_current(self):
        return (self.curr_coord, self.prev_direction, self.prev_step_count, self.curr_temp)

    def get_list_of_potential_next_steps(self):
        potential_next_steps = []
        for i in range(self.single_direction_limit_min, self.single_direction_limit_max + 1):
            for direction in self.directions:
                next_coord = self.get_next_coord(i, direction)
                if not self.is_valid_next_coord(i, direction, next_coord):
                    continue
                if next_coord == (0, 0):
                    continue

                next_temperature = self.calculate_temperature(i, direction)
                next_prev_direcion = self.get_opposite_direction(direction)
                next_prev_step_count = i

                if next_prev_direcion == self.prev_direction:
                    next_prev_step_count += self.prev_step_count

                next = (next_coord, next_prev_direcion,
                        next_prev_step_count, next_temperature)

                if next[:-1] not in self.seen:
                    potential_next_steps.append(next)

        return potential_next_steps

    def calculate_temperature(self, steps, direction):
        temperature = self.curr_temp
        # print('TEMPERATURE', temperature)
        passing_thougt_coords = []
        for i in range(1, 1 + steps):
            passing_thougt_coords.append(self.get_next_coord(i, direction))

        i = 0
        for each in passing_thougt_coords:
            temperature += self.field[each[0]][each[1]]
        # print('TEMPERATURE', temperature)
        return temperature

    def is_valid_next_coord(self, steps, direction, next_coord):
        if self.is_coord_outside_of_the_bound(next_coord):
            return False

        if direction == self.prev_direction:
            return False

        if direction == self.get_opposite_direction_form_prev():
            if steps + self.prev_step_count > self.single_direction_limit_max:
                return False

            if steps + self.prev_step_count < self.single_direction_limit_min:
                return False
        return True

    def get_opposite_direction_form_prev(self):

        self.opposite_direcion_form_prev = self.get_opposite_direction(
            self.prev_direction)

        return self.opposite_direcion_form_prev

    def get_opposite_direction(self, direction):
        if direction == 'up':
            return 'down'
        elif direction == 'right':
            return 'left'
        elif direction == 'right':
            return 'left'
        elif direction == 'down':
            return 'up'
        elif direction == 'left':
            return 'right'
        else:
            print('Not a valid direction: ', direction,
                  '\n "up", "right", "down", or "left" expected')
            raise Exception("Direction error")

    def get_previous_coord(self):
        return self.get_coordinate(self.curr_coord, self.prev_step_count, self.prev_direction)

    def get_next_coord(self, steps, direction):
        return self.get_coordinate(self.curr_coord, steps, direction)

    def get_coordinate(self, current, steps, direction):
        coord0 = current[0] + \
            self.directions[direction][0] * steps

        coord1 = current[1] + \
            self.directions[direction][1] * steps

        return (coord0, coord1)

    def is_coord_outside_of_the_bound(self, coord):
        if coord[0] < 0 or coord[0] >= len(self.field):
            return True
        if coord[1] < 0 or coord[1] >= len(self.field[0]):
            return True

        return False
