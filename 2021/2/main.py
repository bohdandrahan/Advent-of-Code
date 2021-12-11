from input_reader import Input_Reader;
from location_calculator import Location_Calculator;

file = Input_Reader("input.txt");

calculator = Location_Calculator(file.get_list())
calculator.print_result()
calculator.calculate2()
calculator.print_result()