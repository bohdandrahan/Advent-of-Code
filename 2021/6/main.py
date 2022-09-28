from input_reader import Input_Reader;
from fish_calculator import Fish_Calculator;

file = Input_Reader('input.txt')
print("input: ", file.get_list())

calculator = Fish_Calculator(file.get_list(), 80)

calculator.run_all_gens()
calculator = Fish_Calculator(file.get_list(), 256)
calculator.format_dict()
calculator.run_all_gens_dict()
