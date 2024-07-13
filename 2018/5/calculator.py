import pandas as pd


def elements_collide(one, another):
    if one != another and one.upper() == another.upper():
        return True
    return False


def removed_polymer(polymer, element):
    new_polymer = polymer[:]
    new_polymer = new_polymer.replace(element.lower(), "")
    new_polymer = new_polymer.replace(element.upper(), "")
    return new_polymer


def get_collapsed_polymer(polymer):

    collapsed_polymer = ""
    i = 0
    while i < len(polymer):
        if not collapsed_polymer:
            collapsed_polymer = polymer[i]
            i += 1
            continue

        if elements_collide(polymer[i], collapsed_polymer[-1]):
            collapsed_polymer = collapsed_polymer[:-1]
            i += 1
            continue

        else:
            collapsed_polymer += polymer[i]
            i += 1

    return collapsed_polymer


class Calculator():
    def __init__(self, df):
        self.df = df

    def calculate1(self):
        polymer = self.df.at[0, 0]

        return len(get_collapsed_polymer(polymer))

    def calculate2(self):

        polymer = self.df.at[0, 0]

        elements = 'abcdefghijklmnopqrstuvwxyz'

        min_polymer_len = float('inf')

        for element in elements:
            current_polymer = removed_polymer(polymer, element)

            min_polymer_len = min(min_polymer_len,
                                  len(get_collapsed_polymer(current_polymer)))

        return min_polymer_len
