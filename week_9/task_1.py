from random import randint

class Hand(object):
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        hand_string = []
        for card in self.cards:
            hand_string.append(str(card))
        return "\n".join(hand_string)

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.index = randint(0, 51)

    def __str__(self):
        return self.value + " of " + self.suit

class Deck(object):
    suits = [
        'Spades',
        'Hearts',
        'Clubs',
        'Diamonds'
    ]

    values = [
        'Ace',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten',
        'Jack',
        'Queen',
        'King'
    ]
    
    def __init__(self):
        self.cards = []
        for n in range(0, 52):
            self.cards.append(Card(self.suits[n // 13], self.values[n % 13]))

    def __str__(self):
        deck_string = []
        for card in self.cards:
            deck_string.append(str(card))
        return "\n".join(deck_string)

    def shuffle(self):
        self.cards.sort(key = lambda x : x.index)

    def deal_hand(self, num_cards = 5):
        hand = []
        for n in range(0, num_cards):
            hand.append(self.cards.pop())
        return Hand(hand)


deck = Deck()
deck.shuffle()
hand = deck.deal_hand(num_cards = 7)
print(hand)
