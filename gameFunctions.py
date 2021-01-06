def askNum(question, lo, hi):
    response = None
    while response not in range(lo, hi):
        response = int(input(question))
    return response

def getName(question):
    while True:
        name = input(question)
        if (len(name) >= 2) and (len(name) <= 10):
            return name
        else:
            wrongChoice()

def nextTurn(turn):
    if turn == 1:
        return 0
    else:
        return 1

def askYesNo(question):
    """Ask a yes or no question and get back a binary answer."""
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(question).lower()
    return response

class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = Score()
        self.lives = 3

class Score(object):
    def __init__(self):
        self.value = 0
        self.step = 10

    def add(self,itemid):
        for i in range(itemid):
            self.value += self.step

    def subtract(self,itemid):
        for i in range(itemid):
            self.value -= self.step
            if self.value < 0:
                self.value = 0

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")