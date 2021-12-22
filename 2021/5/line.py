
class Line():
    def __init__(self, start_point, end_point):
        self.start_point = start_point;
        self.end_point = end_point;
        self.points = list()
        self.calculate_all_points()
    
    def calculate_all_points(self):
        if self.start_point[0] == self.end_point[0]:
            self.calculate_positions(1)
        elif self.start_point[1] == self.end_point[1]:
            self.calculate_positions(0)
        else:
            self.calculate_diagonal_position()
        
    def calculate_positions(self, axis):
        min_point = min(self.start_point[axis], self.end_point[axis])
        max_point = max(self.start_point[axis], self.end_point[axis])
        for each in range(min_point, max_point + 1):
            if axis == 1:
                self.points.append((self.start_point[0],each))
            elif axis == 0:
                self.points.append((each, self.start_point[1]))
            else: raise Exception("Axis is invalid")
    
    def calculate_diagonal_position(self):
        s = self.start_point
        e = self.end_point

        if s[0]<e[0] and s[1]<e[1]:
            self.calculate_diagonal_up(s, e)
        elif s[0]<e[0] and s[1]>e[1]:
            self.calculate_diagonal_down(s, e)
        elif s[0]>e[0] and s[1]>e[1]:
            self.calculate_diagonal_up(e, s)
        elif s[0]>e[0] and s[1]<e[1]:
            self.calculate_diagonal_down(e, s)
        
    def calculate_diagonal_up(self, start, end):
        for each, point_pos in enumerate(range(start[0], end[0]+1)):
            self.points.append((start[0]+each, start[1]+each))
    
    def calculate_diagonal_down(self, start, end):
        for each, point_pos in enumerate(range(start[0], end[0]+1)):
            self.points.append((start[0]+each, start[1]-each))



    
    def get_points(self):
        return self.points

