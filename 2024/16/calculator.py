import heapq

class Calculator():
    def __init__(self, data, debugger = False):
        self.debugger = debugger

        self.data = data
        # self.pr(data)

        self.directions = [[0,1],[1,0],[0,-1],[-1,0]]

    def calculate1(self):
        print('calculate 1 is running')
        priority_que = []
        heapq.heapify(priority_que)
        current_pos = self.data["start_pos"]
        current_dir = self.directions[0] #init direction is east
        seen = set()


        while current_pos != self.data["end_pos"]:
            if tuple(current_pos + current_dir) in seen:
                continue
            else:
                seen.add(tuple(current_pos + current_dir))

            for direction in self.directions:
                turning_points = 0
                if current_dir == [-direction[0], -direction[1]]: #we can't go backwards
                    continue

                #TODO: do the dijkstra's algoritm


        return 

    def calculate2(self):
        print('calculate 2 is running')

        return
    
    def pr(self, content_to_print):
        if self.debugger:
            print(content_to_print)

    def do_next_step(self, priority_que, 
