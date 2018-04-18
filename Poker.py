#  File: Poker.py

#  Description: Play a game of poker with up to 6 players. The Player with the strongest hand will win, or tie with someone else.

#  Student's Name: Changjie Lan

#  Student's UT EID: cl38442

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51340

#  Date Created: 2/7/18

#  Date Last Modified: 2/9/18
import random
#create card class
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)
#create deck class
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)
#create poker class
class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)
    print()
    # create list to store value and total points 
    h=0
    total_point=0
    winner=[]
    point_hand=[]
    # determine the hand strength
    # also determine the hand value of each player's hand, stored in total_point
    for i in range (len(self.players)):
      types=""
      #implements the user defined functions straight flush, royal flush etc. 
      if self.is_royal(self.players[i]):
        types="Royal Flush"
        h=10
        total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_straight_flush(self.players[i]):
        types="Straight Flush"
        h=9
        total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_four_kind(self.players[i]):
        types="Four of a Kind"
        h=8
        user=[]
        for card in self.players[i]:
          user.append(card.rank)
        if user.count(self.players[i][0].rank)==1:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][2].rank * 13 + self.players[i][0].rank          
        elif user.count(self.players[i][4].rank)==1:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][2].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_full_house(self.players[i]):
        types="Full House"
        h=7
        user=[]
        for card in self.players[i]:
          user.append(card.rank)
        if user.count(self.players[i][0].rank)==3:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        elif user.count(self.players[i][-1].rank)==3:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][0].rank * 13 + self.players[i][1].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_flush(self.players[i]):
        types="Flush"
        h=6
        total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_straight(self.players[i]):
        types="Straight"
        h=5
        total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_three_kind(self.players[i]):
        types="Three of a Kind"
        h=4
        user=[]
        for card in self.players[i]:
          user.append(card.rank)
        if user.count(self.players[i][1].rank)==3 and user.count(self.players[i][2].rank)==3 and user.count(self.players[i][3].rank)==3:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][0].rank * 13 + self.players[i][4].rank
        elif user.count(self.players[i][0].rank)==3:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        else:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][0].rank * 13 + self.players[i][1].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_two_pair(self.players[i]):
        types="Two Pair"
        h=3
        user=[]
        for card in self.players[i]:
          user.append(card.rank)
        if user.count(self.players[i][0].rank)==2 and user.count(self.players[i][2].rank)==2:
          total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        elif user.count(self.players[i][2].rank)==1:
          total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][3].rank * 13**2 + self.players[i][4].rank * 13 + self.players[i][2].rank
        elif user.count(self.players[i][0].rank)==1:
          total_point= h * 13**5 + self.players[i][1].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][3].rank * 13**2 + self.players[i][4].rank * 13 + self.players[i][0].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_one_pair(self.players[i]):
        types="One Pair"
        h=2
        user=[]
        for card in self.players[i]:
          user.append(card.rank)
        if user.count(self.players[i][0].rank)==2 and user.count(self.players[i][1].rank)==2:
          total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        elif user.count(self.players[i][1].rank)==2 and user.count(self.players[i][2].rank)==2:
          total_point= h * 13**5 + self.players[i][1].rank * 13**4 + self.players[i][2].rank * 13**3 + self.players[i][0].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        elif self.players[i][2].rank==self.players[i][3].rank:
          total_point= h * 13**5 + self.players[i][2].rank * 13**4 + self.players[i][3].rank * 13**3 + self.players[i][0].rank * 13**2 + self.players[i][1].rank * 13 + self.players[i][4].rank
        else:
          total_point= h * 13**5 + self.players[i][3].rank * 13**4 + self.players[i][4].rank * 13**3 + self.players[i][0].rank * 13**2 + self.players[i][1].rank * 13 + self.players[i][2].rank
        winner.append(h)
        point_hand.append(total_point)
      elif self.is_high_card(self.players[i]):
        types="High Card"
        h=1
        total_point= h * 13**5 + self.players[i][0].rank * 13**4 + self.players[i][1].rank * 13**3 + self.players[i][2].rank * 13**2 + self.players[i][3].rank * 13 + self.players[i][4].rank
        winner.append(h)
        point_hand.append(total_point)
      #prints the hand of each player
      print("Player " +str (i+1) + " : " + types)
    print()
    # determine winner and print
    corresponding=[]
    tiebreaker=[]
    #determine winner if the winner is a unique type of hand
    if winner.count(max(winner))==1:
      print("Player " +str(winner.index(max(winner))+1) + " wins.")
    #tiebreaker scenario when it is not unique
    else:
      for i in range(len(winner)):
        if winner[i]==max(winner):
          corresponding.append(i)
      for j in corresponding:
        tiebreaker.append(point_hand[j])
      tiebreaker= sorted (tiebreaker, reverse=True)
      for k in tiebreaker:
        tie_player = point_hand.index(k)+1
        print("Player", tie_player, "ties.")
        point_hand[point_hand.index(k)]=-1
    print()
      
      
      
  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    
    return (same_suit and rank_order)

  
  def is_straight_flush (self, hand):
    same_suit= True
    for i in range(len(hand)-1):
        same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
    if (not same_suit):
        return False
    rank_order=True
    for i in range (len(hand)):
        rank_order = rank_order and (hand[i].rank == hand[0].rank - i)
    return (same_suit and rank_order)

  def is_four_kind (self, hand):
    same_rank=True
    user=[]
    for card in hand:
      user.append(card.rank)
    if user.count(hand[2].rank)==4:
      same_rank=True
    else:
      same_rank=False
    return same_rank
  
  def is_full_house (self, hand):
    user=[]
    for card in hand:
      user.append(card.rank)
    three_of_a_kind=True
    if user.count(hand[0].rank)== 3 or user.count(hand[-1].rank)==3:
      three_of_a_kind=True
    else:
      return False
    pair=True
    if user.count(hand[0].rank)== 2 or user.count(hand[-1].rank)==2:
      pair=True
    else:
      return False
    
    return three_of_a_kind and pair

  def is_flush (self, hand):
    same_suit=True
    for i in range(len(hand)-1):
        same_suit = same_suit and (hand[i].suit == hand[i+1].suit)
    if (not same_suit):
        return False
    return same_suit
  
  def is_straight (self, hand):
    rank_order=True
    for i in range (len(hand)):
        rank_order = rank_order and (hand[i].rank == hand[0].rank - i)
    if (not rank_order):
        return False
    return rank_order

  def is_three_kind (self, hand):
    three_of_a_kind=True
    user=[]
    for card in hand:
      user.append(card.rank)
    if user.count(hand[2].rank)==3:
      three_of_a_kind=True
    else:
      return False
    return three_of_a_kind

  def is_two_pair (self, hand):
    user=[]
    for card in hand:
      user.append(card.rank)
    if user.count(hand[1].rank)==2 and user.count(hand[3].rank)==2:
      return True
    else:
      return False

  
   #determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False

  
  def is_high_card (self, hand):
      return True


def main():
  #prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))
  print()
  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()
