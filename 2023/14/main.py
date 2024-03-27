import sys
import time

from input_reader import Input_Reader
from calculator import Calculator

test_file = Input_Reader('test_input.txt')

try:
    file = Input_Reader('input.txt')
except FileNotFoundError:
    print("ERROR: The file with your puzzle input is expected in the current directory. It should be named 'input.txt'")
    sys.exit()


test_result1 = Calculator(test_file.get_data()).calculate1()
print('Solution for test 1st part: ' + str(test_result1))


start_time = time.time()
result1 = Calculator(file.get_data()).calculate1()
end_time = time.time()
print('Solution for 1st part: ' + str(result1))
execution_time = end_time - start_time
print("Execution time: {:.3f} seconds".format(execution_time))


# test_result2 = Calculator(test_file.get_data()).calculate2()
# print('Solution for test 2nd part: ' + str(test_result2))
# start_time = time.time()
# result2 = Calculator(file.get_data()).calculate2()
# end_time = time.time()
# print('Solution for 2nd part: ' + str(result2))
# execution_time = end_time - start_time
# print("Execution time: {:.3f} seconds".format(execution_time))
