from input_reader import Input_Reader;
from fish_calculator import Fish_Calculator;

file = Input_Reader('input.txt')
print("input: ", file.get_list())

calculator = Fish_Calculator(file.get_list())
calculator.run_all_gens()
