import itertools


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
        networks = []
        for pair in self.data:
            seen = False
            for network in networks:
                for each in network:
                    self.pr(each, pair)
                    if each == pair[0] or each == pair[1]:
                        seen = True
                        self.pr("TRUEEEEE")
                        break

                if seen:
                    network.update(set(pair))
                    self.pr(network)
                    break

            if not seen:
                networks.append(set(pair))

        result = 0

        all_combinations_of_3 = []
        all_combinations_of_3_full = []
        for network in networks:
            self.pr("network", network, "end of network")

            if len(network) >= 3:
                combinations_of_3 = list(itertools.combinations(network, 3))
                self.pr(combinations_of_3, "COMBO_3")

                for combo_3 in combinations_of_3:

                    all_combinations_of_3_full.append(combo_3)
                    has_tee = False

                    for each in combo_3:
                        if each[0] == 't':
                            self.pr("YES", combo_3)
                            has_tee = True

                    if has_tee:
                        all_combinations_of_3.append(combo_3)
                        break

        self.pr(all_combinations_of_3, 'ALL')
        self.pr(len(all_combinations_of_3))

        self.pr(all_combinations_of_3_full, 'ALL FULL',
                len(all_combinations_of_3_full))
        return len(all_combinations_of_3_full)

    def calculate2(self):

        print('calculate 2 is running')

        return
