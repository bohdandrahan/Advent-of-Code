
class Calculator():
    def __init__(self, data):
        self.data = data
        self.cards = [each[0] for each in self.data]
        self.bids = [each[1] for each in self.data]
        self.card_strength = {'A': '13', 'K': '12', 'Q': '11', 'J': '10', 'T': '09',
                              '9': '08', '8': '07', '7': '06', '6': '05', '5':'04',
                               '4': '03', '3': '02', '2': '01'}
        self.card_strength_part2 = {'A': '13', 'K': '12', 'Q': '11', 'J': '00', 'T': '09',
                              '9': '08', '8': '07', '7': '06', '6': '05', '5':'04',
                               '4': '03', '3': '02', '2': '01'}
                               

    def calculate1(self):

        #calling function inside of lambda. I remember how unintuitive it was the first time I saw lambda functions in python.
        #I wonder if that is going to be a case in a future, because still it is kind of unintuitive, 
        #but at least I understand it. I wonder if there better ways of implementing anonymus functions that are more 
        #intuitive to human brain. Or perhaps to my brain, maybe other people find it easy peasy (hightly doubt). 
        sorted_hands = sorted(self.data, key=lambda hand: self.get_strength(hand[0]))

        result = 0
        for i, each in enumerate(sorted_hands):
            result += int(each[1])*(i+1)
        
        return result

    def get_strength(self, cards):
        strength = ''

        card_counts = {card: cards.count(card) for card in set(cards)}
        card_counts_values = sorted(card_counts.values())

        #Five of a kind, where all five cards have the same label: AAAAA
        if card_counts_values == [5]:
            strength += '7'
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        elif card_counts_values == [1,4]:
            strength += '6'
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        elif card_counts_values == [2,3]:
            strength += '5'
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        elif card_counts_values == [1,1,3]:
            strength += '4'
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        elif card_counts_values == [1,2,2]:
            strength += '3'
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        elif card_counts_values == [1,1,1,2]:
            strength += '2'
        # High card, where all cards' labels are distinct: 23456
        else:
            strength += '1'

        for card in cards:
            strength += self.card_strength[card]
        
        return int(strength)

    def calculate2(self):
        sorted_hands = sorted(self.data, key=lambda hand: self.get_strength_part2(hand[0]))

        result = 0
        for i, each in enumerate(sorted_hands):
            result += int(each[1])*(i+1)
        
        return result

    #I wrote down logic manually just beacuse it seems easier to do it this way. 
    #Alternativelly, I could've replaced all of the 'J' with the hiest occuring card other than jokers for each hand
    def get_strength_part2(self, cards):
        strength = ''

        card_counts = {card: cards.count(card) for card in set(cards)}
        card_counts_values = sorted(card_counts.values())

        #Five of a kind, where all five cards have the same label: AAAAA
        if card_counts_values == [5]:
            strength += '7'
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        elif card_counts_values == [1,4]:
            if 'J' in cards:
                strength += '7'
            else:
                strength += '6'
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        elif card_counts_values == [2,3]:
            if 'J' in cards:
                strength += '7'
            else:
                strength += '5'
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        elif card_counts_values == [1,1,3]:
            if 'J' in cards:
                strength += '6'
            else: 
                strength += '4'
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        elif card_counts_values == [1,2,2]:
            if 'J' in cards:
                if card_counts['J'] == 1:
                    strength+= '5'
                else:
                    strength += '6'
            else: 
                strength += '3'
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        elif card_counts_values == [1,1,1,2]:
            if 'J' in cards:
                strength += '4'
            else: strength += '2'
        # High card, where all cards' labels are distinct: 23456
        else:
            if 'J' in cards:
                strength += '2'
            else: 
                strength += '1'

        for card in cards:
            strength += self.card_strength_part2[card]
        
        return int(strength)
