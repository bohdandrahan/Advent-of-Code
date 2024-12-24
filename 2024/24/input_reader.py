from typing import DefaultDict


class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.data = {"inputs": {}, "logic_gates": []}

        input_part = True
        for i, line in enumerate(self.file):
            if line == "\n":
                input_part = False
                continue

            if input_part:
                # Example of a line: "x00: 1"
                line = line.strip().split(r": ")
                wire = line[0]
                wire_output = int(line[1])
                self.data["inputs"][wire] = wire_output
            else:
                # Example of a line: "x00 AND y00 -> z00"
                line = line.strip().split(" ")
                input_wires = [line[0], line[2]]
                operator = line[1]
                output_wire = line[-1]
                self.data["logic_gates"].append(
                    {"input_wires": input_wires, "operator": operator, "output_wire": output_wire})

    def get_data(self):
        return self.data
