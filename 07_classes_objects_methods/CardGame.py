"""
Program where user can select to play different card games

Card game 1: High Card:
Both player and computer draws a card from a deck of 52 cards.
High card wins, ties are determined by suit (Spade > Heart > Diamond > Club)

Card game 2: Black Jack:
Both player and computer are dealt 2 cards.  Player and computer can chose to draw more cards.
Whoever's hand adds up closest to 21 without going over wins
Aces count as 1 or 11

"""
import random

# Class to represent individual cards
class Card:
    def __init__(self, suit, value):
        self.suit = suit    # suit is an int value, 0 = clubs, 1 = diamonds, 2 = hearst, 3 = spades
        self.value = value

    def __str__(self):
        """ Returns card value and suit """
        if self.value == 1:
            return f"Ace of {self.getSuit()}"
        elif self.value == 11:
            return f"Jack of {self.getSuit()}"
        elif self.value == 12:
            return f"Queen of {self.getSuit()}"
        elif self.value == 13:
            return f"King of {self.getSuit()}"
        return f"{self.value} of {self.getSuit()}"

    def getSuit(self):
        """ returns the suit of the card """
        if self.suit == 0:
            return "Clubs"
        elif self.suit == 1:
            return "Diamonds"
        elif self.suit == 2:
            return "Hearts"
        elif self.suit == 3:
            return "Spades"

# Class to represent a deck of cards
class Deck:
    def __init__(self):
        """ creates a deck of 52 cards """
        self.cards = []
        for suit in range(4):               # add all 4 suits to deck
            for value in range(1, 14):      # add Ace through King for each suit to deck
                self.cards.append(Card(suit, value))

    def __str__(self):
        """ prints how many cards are left in the deck """
        return f"\nThere are {self.cardRemaining()} cards remaining in the deck."

    def shuffle(self):
        """ Shuffles the deck of cards """
        random.shuffle(self.cards)
        print("\nDeck has been shuffled.")

    def drawCard(self):
        """ removes the first card from the deck and returns it """
        if self.cardRemaining() == 0:
            print("\nSorry, there are no more cards in the deck.")
            return None
        return self.cards.pop(0)

    def cardRemaining(self):
        """ returns the number of cards left in the deck """
        return len(self.cards)

# Subclass of Deck for High Card game
class highCard(Deck):
    def __init__(self, pname):
        super().__init__()
        # initialize players of the game and their respective cards
        self.pname = pname
        self.computer = "Computer"
        self.players = {pname: None, "Computer": None}

    def play(self):
        """ deals one card to each player and computer """
        self.shuffle()          # shuffle first before dealing
        self.players[self.pname] = self.drawCard()          # player draws card
        self.players[self.computer] = self.drawCard()       # computer draws card
        print(f"\n{self.pname} drew a {self.players[self.pname]}, Computer drew a {self.players[self.computer]}")

    def winner(self):
        """ determines the winner """
        if self.players[self.pname].value > self.players[self.computer].value:
            print(f"\n{self.pname} is the winner!")
        elif self.players[self.computer].value > self.players[self.pname].value:
            print(f"\nComputer is the winner!")
        else:           # in event of a tie, use suits as tiebreaker
            if self.players[self.pname].getSuit() > self.players[self.computer].getSuit():
                print(f"\n{self.pname} is the winner! (Tiebreaker - {self.players[self.pname].getSuit()} is higher than {self.players[self.computer].getSuit()})")
            elif self.players[self.computer].getSuit() > self.players[self.pname].getSuit():
                print(f"\nComputer is the winner! (Tiebreaker - {self.players[self.computer].getSuit()} is higher than {self.players[self.pname].getSuit()})")
        self.reset()    # discard hands

    def reset(self):
        """ resets the hands of all players """
        for i in self.players:
            self.players[i] = None

class blackJack(Deck):
    def __init__(self, pname):
        super().__init__()
        self.pname = pname
        self.playerHand = []
        self.dealerHand = []
        self.input = "string"
        self.gameOver = False

    def dealCards(self):
        """ deal initial hand """
        for i in range(2):
            self.playerHand.append(self.drawCard())
            self.dealerHand.append(self.drawCard())

    def broadcast(self):
        """ broadcasts current game information """
        print(f"\nDealer has a {self.dealerHand[0]} showing")
        print(f"\n{self.pname} has the following cards:")
        for i in self.playerHand:
            print(i)
        print(f"Total value is {self.calTotal(self.playerHand)}")

    def calTotal(self, player: list):
        """ calculates total value of hand and returns it """
        total = 0            # stores total value
        aces = 0            # keeps track of aces in hand.  Will add those last
        for card in player:
            if card.value == 11 or card.value == 12 or card.value == 13:    # jacks, queens, kings only add 10
                total += 10
            elif card.value == 1:
                aces += 1
            else:
                total += card.value
        for i in range(aces):       # add value of aces to total
            if total + 11 > 21:     # if ace = 11 value causes bust, set ace value to 1
                total += 1
            else:
                total += 11
        return total

    def isBust(self, player: list):
        """ determines if hand is a bust, return True for yes, False for no """
        if self.calTotal(player) > 21:
            return True
        else:
            return False

    def dealerTurn(self):
        """ Logic for dealer hitting/staying """
        print(f"\nDealer has {self.dealerHand[0]} and {self.dealerHand[1]}")
        print(f"Dealer's total value is {self.calTotal(self.dealerHand)}\n")
        while self.calTotal(self.dealerHand) < 17:          # dealer must hit when total is below 17
            self.dealerHand.append(self.drawCard())
            print(f"Dealer is dealt a {self.dealerHand[-1]}, total value is no {self.calTotal(self.dealerHand)}")
        self.gameOver = True

    def winner(self):
        """ determines who is the winner """
        if self.isBust(self.playerHand):
            print(f"\n{self.pname} busted! Dealer wins.")
        elif self.isBust(self.dealerHand):
            print(f"\nDealer busted! {self.pname} wins.")
        elif self.calTotal(self.dealerHand) > self.calTotal(self.playerHand):   # dealer wins if total is higher than player
            print(f"Dealer has {self.calTotal(self.dealerHand)}, {self.pname} has {self.calTotal(self.playerHand)}. Dealer wins!")
        elif self.calTotal(self.playerHand) > self.calTotal(self.dealerHand):   # player wins if total is higher than dealer
            print(f"{self.pname} has {self.calTotal(self.playerHand)}, dealer has {self.calTotal(self.dealerHand)}. {self.pname} wins!")
        else:
            print("Push. Both players have the same total")

    def reset(self):
        """ resets all hands """
        self.dealerHand = []
        self.playerHand = []

    def play(self):
        """ main function controlling game play logic """
        self.gameOver = False
        self.reset()
        while not self.gameOver:
            self.shuffle()                  # shuffle deck first
            self.dealCards()                # deal initial hand
            self.broadcast()                # broadcast current game information
            while True:                     # as long as player wants to hit...
                self.input = input("\nPress any key to hold, enter [hit] to draw a card: ")
                if self.input.lower() != "hit":     # breaks out if player wants to hold
                    break
                self.playerHand.append(self.drawCard())     # draw a card
                self.broadcast()
                if self.isBust(self.playerHand):                 # if player busted, then game is over and determine winner
                    self.gameOver = True
                    break
            if self.gameOver:
                break
            self.dealerTurn()               # dealer's turn to hit/hold

# Main Code

user_input = input("""Please select between one of the following two cards games:

Card game 1 - High Card: (Enter 1)
Both player and computer draws a card from a deck of 52 cards.
High card wins, ties are determined by suit (Spade > Heart > Diamond > Club)

Card game 2 - Black Jack: (Enter 2)
Both player and dealer are dealt 2 cards.  
Player can chose to draw more cards.  Dealer must hit if < 17
Whoever's hand adds up closest to 21 without going over wins
Aces count as 1 or 11

Make your selection: """)

while (user_input != "1") and (user_input != "2"):
    user_input = input("\nInvalid Selection, please select again: ")

player_name = input("\nPlease enter your name: ")

if user_input == "1":
    game = highCard(player_name)
if user_input == "2":
    game = blackJack(player_name)

while game.cardRemaining() > 0:
    game.play()
    game.winner()
    print(game)
    user_input = input("\nPress any key to continue playing, press N to quit: ")
    if user_input.lower() == "n":
        break

