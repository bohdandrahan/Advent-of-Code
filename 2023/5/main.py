from input_reader import Input_Reader;
from calculator import Calculator;

test_file = Input_Reader('test_input.txt')
test_result1 = Calculator(test_file.get_list()).calculate1()
# test_result2 = Calculator(test_file.get_list()).calculate2()

print('Solution for test 1st part: ' + str(test_result1))
# print('Solution for test 2nd part: ' + str(test_result2))


# file = Input_Reader('input.txt')
result1 = Calculator(file.get_list()).calculate1()
# result2 = Calculator(file.get_list()).calculate2()

print('Solution for 1st part: ' + str(result1))
# print('Solution for 2nd part: ' + str(result2))
