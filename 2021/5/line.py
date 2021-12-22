
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
            pass
        
    def calculate_positions(self, axis):
        min_point = min(self.start_point[axis], self.end_point[axis])
        max_point = max(self.start_point[axis], self.end_point[axis])
        for each in range(min_point, max_point + 1):
            if axis == 1:
                self.points.append((self.start_point[0],each))
            elif axis == 0:
                self.points.append((each, self.start_point[1]))
            else: raise Exception("Axis is invalid")
    
    def get_points(self):
        return self.points

