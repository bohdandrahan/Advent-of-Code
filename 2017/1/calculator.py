
class Calculator():
    def __init__(self, data, debugger=False):
        self.debugger = debugger

        self.data = data
        self.pr(data)

    def pr(self, *content_to_print):
        if self.debugger:
            print(*content_to_print)

    def calculate1(self):
        result = 0
        for i, each in enumerate(self.data):
            if i == len(self.data) - 1 and self.data[i] == self.data[0] and len(self.data) > 1:
                result += self.data[i]
            elif i >= len(self.data) - 1:
                break

            elif self.data[i] == self.data[i + 1]:
                result += self.data[i]
        return result

    def calculate2(self):
        result = 0
        self.pr(2222)
        for i, each in enumerate(self.data):
            j = (i+len(self.data)//2) % len(self.data)
            self.pr(j, i)

            if self.data[i] == self.data[j]:
                self.pr(i, "I")
                result += self.data[i]
        return result
