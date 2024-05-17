import random


class Card:
     SUITS = ["♣", "♦", "♥", "♠"]
     RANKS = [ "2", "3", "4", "5", "7", "8", "9", "10", "J", "Q", "K", "A"]

     def __init__(self, rank, suit):
         if rank not in self.RANKS:
             raise Exception(f"invalid rank, must be one of {self.RANKS}")
         if suit not in self.SUITS:
             raise Exception(f"invalid suit, must be one of {self.SUITS}")
         self._rank = rank
         self._suit = suit

     @property
     def suit(self):
         return self._suit
# method allows you to get result withut calling it, shortcut
# difference bewteen string and str


     @property
     def rank(self):
         return self._rank

     def __str__(self):
         return f"{self.rank}{self.suit}"
     def __repr__(self):
         return self.__str__()

# magic methods becasue end in 2 underscore
# two methods

class Deck:
    def __init__(self):
        cards = []
        # iterate over all ranks and suits
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

# created class thats all cards
# daved as tuple and not list becasue you can change a list but cant change a taple (avoid cheatig in game)
    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        # shuffles the cards in deck
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

        # shuffles the cards in deck, take list of cards and mixing in random order


class Hand:
    def __init__(self, deck):
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)    

@property
def is_flush(self):
    suit = self._cards[0].suit
    for i in range(1, 5):
        if self._cards[i].suit != suit:
            return False
        return True

while True:
    d = Deck()
    d.shuffle()
    hand = Hand(d)
    if hand.is_flush:
        print("found a flash")
        print(hand)
        break















