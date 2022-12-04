from input_reader import Input_Reader;
from calculator import Calculator;

# file = Input_Reader('input.txt')
file = Input_Reader('test_input.txt')

calculator = Calculator(file.get_data())
