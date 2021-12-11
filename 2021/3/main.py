from epsilon_calculator import Epsilon_Calculator;
from input_reader import Input_Reader;

input = Input_Reader('input.txt').get_list();

calculator = Epsilon_Calculator(input);
calculator.print_result();
