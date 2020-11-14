# Black Jack Game
# A little bit changes to commit again

import random  

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

playing = True # playing a new betting game

# define attribute every single card 
class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
    
# Deck contain 52 cards 
class Deck():
    
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def __str__(self):
        single_card = ''
        for card in self.all_cards:
            single_card += '\n' + card.__str__()
        
        return "The Deck has: " + single_card
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

# player's hand
class Hand():
    
    def __init__(self):
        self.all_cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.all_cards.append(card)
        self.value += card.value
        
        if card.rank == "Ace":
            self.aces += 1
    
    def check_ace(self):
        
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

# player's chip
class Chip():
    
    def __init__(self, total):
        self.total = total
        self.bets = 0
    
    def win_bets(self):
        self.total += self.bets
    
    def loose_bets(self):
        self.total -= self.bets
    
# take bet chip and check for legebility
def take_bets(chips):
    chips.bets = input("How much chips you want to bet: ")
    while True:
        if chips.bets.isdigit() and int(chips.bets) == 0:
            chips.bets = input("Chips at least is greater the zero: ")
        elif chips.bets.isdigit() and int(chips.bets) > chips.total:
            chips.bets = input("You dont have enough chips to bet! Again girl: ")
        elif chips.bets.isdigit() and int(chips.bets) <= chips.total:
            chips.bets = int(chips.bets)
            break
        else:
            chips.bets = input("It is not a number! Again girl: ")
        
# hit card to player
def hit(deck, hand):
    
    hand.add_card(deck.deal_one())
    hand.check_ace()
    
# player choice to hit or stand card
def hit_or_stand(deck, hand):
    
    global playing
    
    while True:
        hit_stand = input("Do you wanna Hit or Stand? H/S: ")
        if hit_stand[0].upper() == 'H':
            hit(deck, hand)
        elif hit_stand[0].upper() == 'S':
            print("Player stands, Dealer's turn")
            playing = False
        else:
            print("Sorry just H or S")
            continue
        
        break

# display card information

def show_some(dealer, player):
    
    print("------DEALER HAND (one card hidden)------")
    print(dealer.all_cards[0])
    print("------PLAYER HAND (both)------")
    for player_card in player.all_cards:
        print(player_card)
    
def show_all(dealer, player):
    
    print("------DEALER HAND (all card)------")
    for dealer_card in dealer.all_cards:
        print(dealer_card)
    
    print("------PLAYER HAND (all card)------")
    for player_card in player.all_cards:
        print(player_card)

# handle game scenario
def player_win(chips):
    print("Player win!")
    chips.win_bets()

def player_bust(chips):
    print("Dealer win!")
    chips.loose_bets()

def dealer_win(chips):
    print("Dealer win!")
    chips.loose_bets()

def dealer_bust(chips):
    print("Player win!")
    chips.win_bets()

def push():
    print("Both are tie! PUSH")
 
# Game logic

 # give player chips
player_chips = Chip(100)
         
while True:
    
    print("Welcome to BlackJack!")
    
    
    # create deck
    new_deck = Deck()
    new_deck.shuffle()
    
    # create player and dealer
    player = Hand()
    dealer = Hand()
    
    # player bets
    take_bets(player_chips)
    
    # intially 2 cards for both
    for i in range(0, 2):
        player.add_card(new_deck.deal_one())
        dealer.add_card(new_deck.deal_one())
        
    while playing == True:
   
        # show cards
        show_some(dealer, player)
            
        # hit or stand
        hit_or_stand(new_deck, player)
        
        # show cards
        show_some(dealer, player)        
    
        # check player's cards values
        if player.value > 21:
            player_bust(player_chips)
            break
        
    if player.value <= 21:
        
        while dealer.value < player.value:
            hit(new_deck, dealer)
        
        # show all cards
        show_all(dealer, player)
        
        if dealer.value > 21:
            dealer_bust(player_chips)
        elif dealer.value > player.value:
            player_bust(player_chips)
        elif dealer.value < player.value:
            player_win(player_chips)
        else:
            push()
        
        
    # inform player's chips total 
    print("Player now has total {one} chips".format(one = player_chips.total))
    if player_chips.total == 0:
        print("Your chips is zero, having no effort to continue! Ppp")
        break
    # ask to play again
    new_game = input("Do you wanna play again? Y/N: ")
    
    if new_game[0].upper() == 'Y':
        playing = True
        continue
    else: 
        print("Thanks for spending your time with us! See yaaa")
        break
                    
    
