import pandas as pd


def has_exactly_N_of_any_letter(word, n):
    for each in word:
        if word.count(each) == n:
            return True
    return False


def get_number_differnce(word1, word2):
    diff = 0
    for i, each in enumerate(word1):
        if each != word2[i]:
            diff += 1
    return diff


def get_common_word(word1, word2):
    word = ""
    for i, each in enumerate(word1):
        if each == word2[i]:
            word += each
    return word


class Calculator():
    def __init__(self, data):
        self.data = data

    def calculate1(self):

        self.data['has_exactly_two'] = self.data[0].apply(
            has_exactly_N_of_any_letter, args=([2]))

        self.data['has_exactly_three'] = self.data[0].apply(
            has_exactly_N_of_any_letter, args=([3]))

        return self.data['has_exactly_two'].sum() * self.data['has_exactly_three'].sum()

    def calculate2(self):

        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if get_number_differnce(self.data[0][i], self.data[0][j]) == 1:
                    return get_common_word(self.data[0][i], self.data[0][j])

        return -1
