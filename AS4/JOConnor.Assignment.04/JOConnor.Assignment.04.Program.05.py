import random


def main():
    playingcards = deck()
    playingcards.shuffle()
    print("Card Dealer\n\nI have shuffled a deck of " + str(playingcards.getSize()) + " cards")
    num = int(input("\nHow many cards would you like?: "))
    print("\nHere are your cards:")
    for i in range(num):
        print(playingcards.deal())
    print("\nThere are " + str(playingcards.getSize()) + " cards left in the deck.\n\nGood Luck")


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
        return self.cards.pop().toString()

    def getSize(self):
        return len(self.cards)


class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def toString(self):
        return self.rank + " of " + self.suit


main()
