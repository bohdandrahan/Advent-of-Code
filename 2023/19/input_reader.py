from .instructions import Instruction_node


class Input_Reader():
    def __init__(self, file_path):
        self.file = open(file_path)
        self.convert_to_list()

    def convert_to_list(self):
        self.workflows = {}
        self.ratings = []

        is_workflow_part = True
        for i, line in enumerate(self.file):
            line = line.strip()

            if not line:
                is_workflow_part = False
                continue

            if is_workflow_part:
                procedure_name, procedure_instructions = line.split('{')

                instruction = Instruction_node()
                instruction = instruction.generate_from_input(
                    procedure_instructions[:-1])

                self.workflows[procedure_name] = instruction

            else:
                rating = {}
                line = line.strip('{}')
                raw_rating = line.split(',')
                for each in raw_rating:
                    rating_key, rating_value = each.split('=')
                    rating_value = int(rating_value)
                    rating[rating_key] = rating_value
                self.ratings.append(rating)

        self.data = [self.workflows, self.ratings]

    def get_data(self):
        return self.data

        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
        ###
