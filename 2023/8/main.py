from input_reader import Input_Reader
from calculator import Calculator

test_file = Input_Reader('test_input.txt')
file = Input_Reader('input.txt')

# test_result1 = Calculator(test_file.get_data()).calculate1()
# print('Solution for test 1st part: ' + str(test_result1))
# result1 = Calculator(file.get_data()).calculate1()
# print('Solution for 1st part: ' + str(result1))

test_result2 = Calculator(test_file.get_data()).calculate2()
print('Solution for test 2nd part: ' + str(test_result2))
result2 = Calculator(file.get_data()).calculate2()
print('Solution for 2nd part: ' + str(result2))
