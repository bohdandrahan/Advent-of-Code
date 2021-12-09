from input_reader import Input_Reader;
from sonar_calculator import Sonar_Calculator;

file = Input_Reader('input.txt')
result = Sonar_Calculator(file.get_list()).calculate()

print(result)