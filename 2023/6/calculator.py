
class Calculator():
    def __init__(self, data):
        self.times = data[0]
        self.distances = data[1]

    def calculate1(self):
        result = 1
        
        for i in range(len(self.times)):
            num_of_beatings = 0

            time = self.times[i]
            distance = self.distances[i]

            for speed in range(time): #speed will be equal to the number of seconds we wait
                range_of_boat = speed * (time-speed)
                if range_of_boat > distance:
                    num_of_beatings += 1
            
            result *= num_of_beatings
        
        return result


    #This one was rather easy
    def calculate2(self):
            num_of_beatings = 0

            time = ''
            for each in  self.times:
                time += str(each)
            time = int(time)

            distance = ''
            for each in  self.distances:
                distance += str(each)
            distance = int(distance)

            for speed in range(time): #speed will be equal to the number of seconds we wait
                range_of_boat = speed * (time-speed)
                if range_of_boat > distance:
                    num_of_beatings += 1
            return num_of_beatings