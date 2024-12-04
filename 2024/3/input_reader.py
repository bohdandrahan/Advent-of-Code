class Input_Reader():
    def __init__(self, file_path):
        with open(file_path, "r") as file:
            file_content = file.read()

        self.file_content = file_content
        self.convert_to_list()

    def convert_to_list(self):
        self.data = self.file_content

    def get_data(self):

        return self.data
