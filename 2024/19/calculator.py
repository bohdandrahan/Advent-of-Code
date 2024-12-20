class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        self.pr(data)

    def calculate1(self):

        print('calculate 1 is running')

        result = 0

        self.seen_map = dict()
        for design in self.data["designs"]:
            is_possible = self.run_matching(design)

            self.pr(
                design, "IS POSSIBLE" if is_possible else "IS NOT POSSIBLE NOT NOT NOT")

            if is_possible:
                result += 1

        return result

    def calculate2(self):
        print('calculate 2 is running')

        return

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def run_matching(self, design):
        if design in self.seen_map:
            return self.seen_map[design]
        is_matching = False

        if len(design) == 0:
            return True

        self.pr(design)

        for pattern in self.data["patterns"]:
            if len(pattern) <= len(design) and pattern == design[:len(pattern)]:
                self.pr('PATTERN CONTINUE', pattern)
                if self.run_matching(design[len(pattern):]):
                    return True

        self.seen_map[design] = is_matching
        return is_matching
