from input_reader import Input_Reader;
from sonar_calculator import Sonar_Calculator;

file = Input_Reader('input.txt')
result1 = Sonar_Calculator(file.get_list()).calculate1()
result2 = Sonar_Calculator(file.get_list()).calculate2()

print('Solution for 1st part: ' + str(result1))
print('Solution for 2nd part: ' + str(result2))