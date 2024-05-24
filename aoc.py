import sys
import os
import time
import importlib


def main():
    if len(sys.argv) < 3 or len(sys.argv) > 5:
        print(
            "Usage: python aoc.py <year> <problem_set_number> [-t or --test] [-partone or -parttwo]")
        return

    year = sys.argv[1]
    problem_set_number = sys.argv[2]
    use_test_input = False
    part_one = False
    part_two = False

    if len(sys.argv) > 3:
        for flag in sys.argv[3:]:
            if flag in ['-t', '--test']:
                use_test_input = True
            elif flag in ['-partone', '-1']:
                part_one = True
            elif flag in ['-parttwo', '-2']:
                part_two = True
            else:
                print(f"Invalid flag: \
                {flag}. Usage: python aoc.py <year> <problem_set_number> [-t or --test] [-partone or -parttwo]")
                return

    try:
        year = int(year)
        problem_set_number = int(problem_set_number)
    except ValueError:
        print("Please enter valid integers for year and problem set number.")
        return

    folder_path = os.path.join(str(year), str(problem_set_number))
    if not os.path.exists(folder_path):
        print(f"Error: Folder for year {year} and problem set \
        {problem_set_number} not found.")
        return

    if use_test_input:
        input_file_path = os.path.join(folder_path, f"test_input.txt")
        print("Using TEST input")
    else:
        input_file_path = os.path.join(folder_path, f"input.txt")

    if not os.path.exists(input_file_path):
        print(f"Error: Input file for year {year} and problem set \
        {problem_set_number} not found.")
        return

    if part_one and part_two:
        print("Please choose either part one or part two, not both.")
        return

    module_name = f"{folder_path}/calculator"

    try:
        module = importlib.import_module(
            module_name.replace('/', '.'), package=f"{folder_path}")
        Calculator = getattr(module, "Calculator")
    except ImportError as e:
        print(f"An error occurred while importing module {module_name}: {e}")
        return

    module_name = f"{folder_path}/input_reader"

    try:
        module = importlib.import_module(
            module_name.replace('/', '.'), package=f"{folder_path}")
        Input_Reader = getattr(module, "Input_Reader")
    except ImportError as e:
        print(f"An error occurred while importing module {module_name}: {e}")
        return

    if part_one:
        print("Running part one of the problem set")
        start_time = time.time()
        result1 = Calculator(Input_Reader(
            input_file_path).get_data()).calculate1()
        end_time = time.time()
        print('Solution for 1st part: ' + str(result1))
        execution_time = end_time - start_time
        print("Execution time: {:.3f} seconds".format(execution_time))

    elif part_two:
        print("Running part two of the problem set")
        start_time = time.time()
        result1 = Calculator(Input_Reader(
            input_file_path).get_data()).calculate2()
        end_time = time.time()
        print('Solution for 2st part: ' + str(result1))
        execution_time = end_time - start_time
        print("Execution time: {:.3f} seconds".format(execution_time))

    else:
        print("Running part one of the problem set")
        start_time = time.time()
        result1 = Calculator(Input_Reader(
            input_file_path).get_data()).calculate1()
        end_time = time.time()
        print('Solution for 1st part: ' + str(result1))
        execution_time = end_time - start_time
        print("Execution time: {:.3f} seconds".format(execution_time))

        print("Running part two of the problem set")
        start_time = time.time()
        result1 = Calculator(Input_Reader(
            input_file_path).get_data()).calculate2()
        end_time = time.time()
        print('Solution for 2st part: ' + str(result1))
        execution_time = end_time - start_time
        print("Execution time: {:.3f} seconds".format(execution_time))


if __name__ == "__main__":
    main()
