from input_reader import Input_Reader;
from calculator import Calculator;

file = Input_Reader('input.txt')

# calculator = Calculator({('acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab') : ['cdfeb','fcadb','cdfeb','cdbaf']})
calculator = Calculator(file.get_dict())
