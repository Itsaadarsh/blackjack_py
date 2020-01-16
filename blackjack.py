'''
DONE BY - AADARSH.S
IG - @aadarshcodes
'''


import  random

suits = {'Hearts','Diamond','Spade','Clubs'}
ranks = {'Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing  = True

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    def __init__(self):
        self.deck = [ ]
        for suit in suits :
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +=  '\n' + card.__str__()
        return  "The Deck has : " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = []
        self.value =0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adj_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self,total=100):
        self.total = total
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True :
        try :
            chips.bet = int(input("How many chips you want to bet : "))
        except:
            print("Enter in integers ")
        else :
            if chips.bet > chips.total :
                print("Sorry you dont have enough chips ")
            else :
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adj_ace()

def hit_or_stand(deck,hand):
    global playing
    while True :
        x = input("Hit or Stand : Enter 'h' or 's' ")
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands dealers turn ")
            playing = False
        else :
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player,dealer,chips):
    print("PLAYER BUST !!")
    chips.lose_bet()
def player_wins(player, dealer, chips):
    print("PLAYER WINS !!")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("DEALER BUST !!")
    chips.win_bet()
def dealer_wins(player, dealer, chips):
    print("DEALER WON !!")
    chips.lose_bet()
def push(player, dealer):
    print("Dealer and player tie!")

while True :
    print("WELCOME TO BLACKJACK...!!\n")
    print("Each player starts with two cards, one of the dealer's cards is hidden until the end.\n"
          "To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.\n"
          "If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.\n")
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21 :
        while dealer_hand.value < 17 :
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else :
            push(player_hand,dealer_hand)

    print("PLayer total chips are : {}".format(player_chips.total))
    new_game = input("Would you like to play again? (y/n) : ")

    if new_game[0].lower() == 'y':
        playing = True
        continue

    else :
        print("thankyou !")
        break
