from input_reader import Input_Reader
from field import Field


input_lines = Input_Reader('input.txt').get_lines()

field = Field()
field.add_lines(input_lines)
field.calculate_number_of_overlaping_points()

print(field.get_number_of_overlaping_points())