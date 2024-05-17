import random


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        cards = []
        # iterate over all ranks and suits, create a card and add it to the list
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        # shuffles the cards in the deck
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

class Hand:
    def __init__(self, deck):
        # deck is shuffled before
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1, 5):
            if self._cards[i].suit != suit:
                return False

        return True

@property
def is_pair(self):
    ranks = []
    for card in self.cards:
        ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
            return False

