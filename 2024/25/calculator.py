class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        # self.pr(data)

        self.pr("KEYS:")
        for key in self.data["keys"]:
            for each in key:
                self.pr(each)
            self.pr('\n')

        self.pr("LOCKS")
        for lock in self.data["locks"]:
            for each in lock:
                self.pr(each)
            self.pr('\n')

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):
        print('calculate 1 is running')

        numeric_keys = list()
        for key in self.data["keys"]:
            numeric_key = [each.count("#") - 1 for each in [list(row)
                                                            for row in zip(*key[::-1])]]
            numeric_keys.append(numeric_key)
            self.pr(numeric_key)

        numeric_locks = list()
        for lock in self.data["locks"]:
            numeric_lock = [each.count("#") - 1 for each in [list(row)
                                                             for row in zip(*lock[::-1])]]
            numeric_locks.append(numeric_lock)
            self.pr(numeric_lock)

        result = 0
        for lock in numeric_locks:
            for key in numeric_keys:
                is_fit = True
                for i in range(5):
                    if key[i] + lock[i] > 5:
                        is_fit = False
                if is_fit:
                    result += 1

        return result

    def calculate2(self):
        print('calculate 2 is running')
        return
