import random

class deck:
    def __init__(self):
        self.cards = []
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        for rank in ranks:
            for suit in suits:
                self.cards.append(card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def getSize(self):
        return len(self.cards)


class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def toString(self):
        return self.rank + " of " + self.suit

    def getRankValue(self):
        match self.rank:
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case "5":
                return 5
            case "6":
                return 6
            case "7":
                return 7
            case "8":
                return 8
            case "9":
                return 9
            case "10":
                return 10
            case "Jack":
                return 10
            case "Queen":
                return 10
            case "King":
                return 10
            case "Ace":
                return 11
