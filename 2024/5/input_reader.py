class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):

        self.rules = []
        self.updates = []

        self.data = [self.rules, self.updates]

        is_rules_phase: bool = True
        for i, line in enumerate(self.file):
            if line == "\n":
                is_rules_phase = False
                continue

            if is_rules_phase:
                formatted_line: list[int] = list(
                    map(lambda x: int(x), line.strip().split("|")))

                self.rules.append(formatted_line)
            else:
                formatted_line: list[int] = list(
                    map(lambda x: int(x), line.strip().split(',')))

                self.updates.append(formatted_line)

    def get_data(self):
        return self.data
