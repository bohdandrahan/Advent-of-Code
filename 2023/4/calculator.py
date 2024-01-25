
class Calculator():
    def __init__(self, data_list):
        self.data = data_list

    def calculate(self, data):
        pass

    def calculate1(self):
        result = 0
        for each in self.data:
            num_of_matches = 0
            for num in each[1]:
                if num in each[0]:
                    num_of_matches += 1
            current_result = 0
            if num_of_matches>0: 
                current_result += 2**(num_of_matches-1)
            
            result += current_result
        return result
        

    #I did not expect I would be able to solve this on a first go. It was challanging but fun.
    #Yesterday it was overwhelming. I guess it is a weird thing with coding.
    #The perception of how hard things are varies depending not on the complexity of the task but on your subjective state at a moment. 
    #What is impossibly hard right now because you feel tiered is going to be a 5 min walk in a park tommorow after a good sleep.
    #Maybe it is even nessesary to sleep over some complex task to allow you intuition to grasp over the problem.
    
    def calculate2(self):
        num_of_tickets = 0

        multipliers = {index: 1 for index in range(len(self.data))}  #I like this syntax. I should use it more

        for i, each in enumerate(self.data):
            num_of_tickets += multipliers[i]
            num_of_matches = 0
            for num in each[1]:
                if num in each[0]:
                    num_of_matches += 1
            if num_of_matches>0:
                for j in range(num_of_matches):
                    multipliers[i+j+1] += multipliers[i]


        return num_of_tickets
                





