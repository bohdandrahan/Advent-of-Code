from operator import delitem


class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        self.pr(data)

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):

        print('calculate 1 is running')

        stack = dict(self.data["inputs"])
        gates = list(self.data["logic_gates"])
        is_not_stale = True

        count = 0
        while is_not_stale:
            is_not_stale = False
            for i, gate in enumerate(gates):
                if gate["input_wires"][0] in stack and gate["input_wires"][1] in stack:
                    logic_result = self.result_of_operation(
                        stack[gate["input_wires"][0]], stack[gate["input_wires"][1]], gate["operator"])
                    stack[gate["output_wire"]] = logic_result
                    is_not_stale = True
                    count += 1
                    gates.pop(i)
                    self.pr("COUNT", count, len(stack))
                    break
        self.pr("STACK", stack)

        is_valid = True
        next = "z00"
        binary_number = ""

        while is_valid:
            binary_number = str(stack[next]) + binary_number
            if len(str(int(next[-2:]) + 1)) == 1:
                filler_zero = "0"
            else:
                filler_zero = ""

            next = "z" + filler_zero + str(int(next[-2:]) + 1)
            is_valid = (next in stack)

            self.pr(stack)

            self.pr(is_valid)

        return int(binary_number, 2)

    def calculate2(self):
        print('calculate 2 is running')
        return

    def result_of_operation(self, input1, input2, operator) -> int:
        if operator == "XOR":
            return input1 ^ input2
        elif operator == "OR":
            return input1 or input2
        elif operator == "AND":
            return input1 and input2

        else:
            return -1
