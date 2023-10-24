from input_reader import Input_Reader;
from calculator import Calculator;

test_file = Input_Reader('test_input.txt')
test_file.printme()

# test_result1 = Calculator(test_file.get_crates(), test_file.get_commands()).calculate1()
# print('Solution for test 1st part: ' + str(test_result1))

test_result2 = Calculator(test_file.get_crates(), test_file.get_commands()).calculate2()
print('Solution for test 2nd part: ' + str(test_result2))


file = Input_Reader('input.txt')
file.printme()

# result1 = Calculator(file.get_crates(), file.get_commands()).calculate1()
# print('Solution for 1st part: ' + str(result1))

result2 = Calculator(file.get_crates(), file.get_commands()).calculate2()
print('Solution for 2nd part: ' + str(result2))

