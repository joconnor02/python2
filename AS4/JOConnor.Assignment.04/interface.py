import business as b

def gameLoop():
    print("Blackjack")
    # Stay in game loop until player quits
    while True:
        # Initialize Deck
        playingcards = b.deck()
        playingcards.shuffle()

        # Deal Opening Hand
        dealhand = [playingcards.deal()]
        playerhand = [playingcards.deal(), playingcards.deal()]
        print("\nDEALER'S SHOW CARD:\n" + dealhand[0].toString())
        print("\nYOUR CARDS:\n" + playerhand[0].toString() + "\n" + playerhand[1].toString() + "\n")

        # Player hit/stand loop
        while True:
            stand = input("Hit or stand? (h/s): ")
            if stand.lower() == "s":
                break
            playerhand.append(playingcards.deal())
            print("\nYOUR CARDS:")
            for cards in playerhand:
                print(cards.toString())
            # Leave the hit stand loop if the player busts
            if getPoints(playerhand) > 21:
                break
        # End the game if the player busts, offer end to game loop
        if getPoints(playerhand) > 21:
                print("Player Bust. Dealer Wins.")
                going = input("\nPlay Again? (y/n)")
                if going.lower() == "n":
                    break
                else:
                    continue
        # The dealer hits until 17
        while getPoints(dealhand) <= 17:
            dealhand.append(playingcards.deal())

        # The Dealer cards are revealed
        print("\nDEALER'S CARDS")
        for cards in dealhand:
            print(cards.toString())
        # The points are totaled and displayed
        print("\nYOUR POINTS:\t" + str(getPoints(playerhand)) + "\nDEALER'S POINTS: " + str(getPoints(dealhand)))

        # If the dealer busted the player wins, offer end to game loop
        if getPoints(dealhand) > 21:
                print("\nDealer Bust. Player Wins.")
                going = input("\nPlay Again? (y/n)")
                if going.lower() == "n":
                    break
                else:
                    continue
        # If the dealer has more points, he wins, else player wins, offer end to game loop
        if getPoints(dealhand) > getPoints(playerhand):
            print("\nDealer Wins")
        else:
            print("\nPlayer Wins")
        going = input("\nPlay Again? (y/n)")
        if going.lower() == "n":
            break

def getPoints(hand):
    sum = 0
    hasAce = False
    for cards in hand:
        sum += cards.getRankValue()
        if cards.getRankValue() == 11:
            hasAce = True
    if sum > 21 and hasAce:
        sum -= 10
    return sum
