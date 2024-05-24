
class Instruction_condition():
    def __init__(self, left, operator, right):
        self.left = left
        self.right = right
        self.operator = operator

    def get_left(self):
        return self.left


class Instruction_node():
    def __init__(self, value=None, condition=None,
                 if_node=None, else_node=None):
        self.value = value
        self.condition = condition,
        self.if_node = if_node,
        self.else_node = else_node

    def generate_from_input(self, input_string: str):
        head = Instruction_node()
        if r'<' in input_string or r'>' in input_string:

            operator = ''
            for char in input_string:
                if char == r'<' or char == r'>':
                    operator = char
                    break

            left, rest = input_string.split(operator, 1)
            right, rest = rest.split(':', 1)
            right = int(right)
            if_node, else_node = rest.split(',', 1)
            head.condition = Instruction_condition(left, operator, right)

            head.if_node = self.generate_from_input(if_node)
            head.else_node = self.generate_from_input(else_node)

        else:
            head.value = input_string

        return head
