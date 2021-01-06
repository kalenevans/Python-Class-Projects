# Kalen Evans
# 12/2020
# Playing Cards Class
import random
class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    SUITS = ["♥", "♦", "♣", "♠"]

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = str.format("""
        +-----------+
        | {1}{0:>2}       |
        |           |
        |           |
        |           |
        |           |
        |       {0:<2}{1} |
        +-----------+
        """,self.rank,self.suit)
        return rep

class Hand(object):
    def __init__(self):
        self.cards = []
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<EMPTY>"
        return rep
    def clear(self):
        self.cards = []
    def add(self,card):
        self.cards.append(card)
    def give(self,card,otherHand):
        self.cards.remove(card)
        otherHand.add(card)

class Deck(Hand):
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def deal(self,hands,perHand=1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard,hand)
                else:
                    print("Deck is out of cards: Clearing hands and reshuffling...")
                    self.clear()
                    self.populate()
                    self.shuffle()
                    for hand in hands:
                        hand.clear()
                    self.deal()

class Pos_Card(Card):
    def __init__(self,rank,suit):
        super(Pos_Card, self).__init__(rank,suit)
        self.faceup = True

    def flip(self):
        self.faceup = not self.faceup

    def __str__(self):
        if self.faceup:
            rep = super(Pos_Card,self).__str__()
        else:
            rep = """
            +-----------+
            |###########|
            |###########|
            |###########|
            |###########|
            |###########|
            |###########|
            +-----------+
            """
        return rep

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")