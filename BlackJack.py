#Kalen Evans
#1/2021
#Black Jack Game
import playing_cards as pc
import gameFunctions as gf

class BJ_Card(pc.Pos_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.faceup:
            v = BJ_Card.RANKS.index(self.rank)+1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(pc.Deck):
    def populate(self):
        for suit in pc.Card.SUITS:
            for rank in pc.Card.RANKS:
                self.add(BJ_Card(rank,suit))

class BJ_Hand(pc.Hand):
    def __init__(self,name):
        super(BJ_Hand, self).__init__()
        self.name = name
        
    def __str__(self):
        print("####################################")
        for card in self.cards:
            print(card)
        rep = "####################################"
        rep += "\n" + self.name
        rep += "\n" + self.total
        return rep
    
    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        for card in self.cards:
            t += card.value
        hasAce = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                hasAce = True
        if hasAce and t <= 11:
            t += 10
        return t
    
    def isBusted(self):
        return self.total > 21
    
class BJ_Player(BJ_Hand):
    def bust(self):
        print(self.name, "busts.")
        self.lose()
    def lose(self):
        print(self.name, "loses.")
    def win(self):
        print(self.name, "wins.")
    def push(self):
        print(self.name, "pushes.")
    def isHitting(self):
        response = gf.askYesNo("\n" + self.name + ", do you want to hit? (Y/N): ")
        return response == "y"
    
class BJ_Dealer(BJ_Hand):
    def isHitting(self):
        return self.total < 17
    
    def bust(self):
        print(self.name, "busts.")
        
    def flipFirstCard(self):
        self.cards[0].flip()
        
class Game(object):
    def __init__(self,names):
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.dealer = BJ_Dealer("Dealer")
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
    
    @property
    def stillPlaying(self):
        sp = []
        for player in self.players:
            if not player.isBusted():
                sp.append(player)
        return sp
    
#testing
deck = BJ_Deck()
deck.populate()
deck.shuffle()

card = deck.cards[0]
print(card)
print(card.value)
