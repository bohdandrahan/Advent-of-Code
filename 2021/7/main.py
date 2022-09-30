from input_reader import Input_Reader;
from crab_calculator import Crab_Calculator;

file = Input_Reader('input.txt')

calculator = Crab_Calculator(file.get_list())

calculator = Crab_Calculator([16,1,2,0,4,2,7,1,2,14])
