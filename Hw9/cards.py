"""Template for CSE 4256 HW9."""

from collections import deque, namedtuple
import csv
from enum import Enum, auto
from random import choice

class Suit(Enum):
    """Enum of the suits of the standard playing cards.

    Each member has two fields: strength and symbol. The strength of a suit defines how it compares
    with other suits; a higher strength will beat a lower strength.
    """

    CLUBS    = (1, '♣')
    DIAMONDS = (2, '♦')
    HEARTS   = (3, '♥')
    SPADES   = (4, '♠')

    def __init__(self, strength, symbol) -> None:
        super().__init__()
        self.strength = strength
        self.symbol = symbol

class Rank(Enum):
    """Enum of the ranks of the standard playing cards.

    Each member has two fields: strength and symbol. The strength of a rank defines how it compares
    to other ranks; a higher strength will beat a lower strength.
    """
    ACE    = (1, 'ACE')
    TWO = (2, 'TWO')
    THREE   = (3, 'THREE')
    FOUR   = (4, 'FOUR')
    FIVE    = (5, 'FIVE')
    SIX = (6, 'SIX')
    SEVEN   = (7, 'SEVEN')
    EIGHT   = (8, 'EIGHT')
    NINE    = (9, 'NINE')
    TEN = (10, 'TEN')
    JACK   = (11, 'JACK')
    QUEEN   = (12, 'QUEEN')
    KING   = (13, 'KING')

    def __init__(self, strength, symbol) -> None:
        super().__init__()
        self.strength = strength
        self.symbol = symbol


Card = namedtuple("Card", ["rank", "suit"])

def card_str(card: Card):
    """Returns a string representing the rank and suit of a playing card."""

    return f"{card.rank.symbol}{card.suit.symbol}"

def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""
    output = deque()
    for i in Rank:
      for j in Suit:
        output.append(Card(i,j))
    return output

def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""

    deck1, deck2 = deque(), deque()

    while len(deck1) < len(deck):
        deck1.append(deck.popleft())

    while 0 < len(deck):
        deck2.append(deck.popleft())

    while len(deck1) > 0 and len(deck2) > 0:
        semi_deck = choice((deck1, deck2))
        deck.append(semi_deck.popleft())

    deck.extend(deck1)
    deck.extend(deck2)

def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""

    for _ in range(7):
        riffle_shuffle(deck)

def deal(deck, n_players):
    """Deals the cards n_players ways."""

    hands = [[] for _ in range(n_players)]
    hand_no = 0
    while len(deck) > 0:
        hands[hand_no].append(deck.pop())
        hand_no = (hand_no + 1) % n_players

    return hands

def play_game(deck: deque, n_players: int, outfile: str):
    """Simulates a simple card game being played by the computer, recording the moves in outfile.

    The rules of the game are as follows:
        - Each round, all players play the card at the top of their hand
        - The player who played the card with the highest rank gets a point
            - If there are multiple cards with the same rank, then suits are taken in reverse
              alphabetical order, with SPADES as the highest suit, then HEARTS, then DIAMONDS,
              then CLUBS. The player with the highest suit (among tied-rank cards) gets a point
        - Once any player's hand is empty, the game is over and the player with the most points
          is declared the winner.

    This function should do the following:
        - Shuffle the deck well
        - Deal the deck into n_players hands (the players have ids 0, 1, 2, ..., n_players - 1)
        - Open a csv file called outfile to which the game will be written
        - Play the game, each round doing the following:
            - Print the cards that were played by each player in this round, as well as the current
              scores of all players and which player won the round
            - Append the round to outfile as a series of rows with one row per card played, keeping
              track of the following:
                - The id of the player who played the card
                - The name of the card Rank (one of "ACE", "TWO", "THREE", "FOUR", "FIVE", etc.)
                - The name of the card Suit (one of "CLUBS", "SPADES", "HEARTS", "DIAMONDS")
        - After the game is over, print the following information about the game:
            - The id of the winning player
            - The scores of all players

    The generated csv file should have the following format:
        - The first row should contain the field names, which are:
            - "player"
            - "rank""
            - "suit"
        - Each subsequent row should contain, in order:
            - The id of the player
            - The name of the rank of the card they played
            - The name of the suit of the card they played
    """
    
    mix_deck(deck)
    hands=deal(deck,n_players)
    score=[]
    with open(outfile, 'w', newline='') as f:
     csvwriter = csv.writer(f)
     csvwriter.writerow(['player', 'rank', 'suit'])
     for i in hands:
       score.append(0)
     while(len(hands[0])!=0):
       high=hands[0][0]
       winningplayer=0
       for i in range(len(hands)):
         curr=hands[i].pop()
         print("Player "+str(i)+" played :"+str(curr[0].symbol)+" of "+ str(curr[1].symbol))
         if(curr==high) :
           winningplayer=i
         else:
           if(curr[0].strength>high[0].strength):
             winningplayer=i
             high=curr
           else:
             if(curr[0].strength==high[0].strength):
               if(curr[1].strength>high[1].strength):
                 high=curr
                 winningplayer=i
       score[winningplayer]+=1
       print("The winner was "+str(winningplayer))
       csvwriter.writerow([winningplayer, high[0].symbol, high[1].symbol])
     winner=0
     high=0
     for i in range(len(score)):
      print("Player "+str(i)+" had score "+str(score[i]))
      if(score[i]>high):
       high=score[i]
       winner=i
     print("The winner is player "+str(i)+" with "+str(high)+" rounds won")

def review_game(infile: str, n_players: int):
    """Reads in a sequence of turns from infile as a CSV file and prints some info about the game.

    The rules of the game are as follows:
        - Each round, all players play the card at the top of their hand
        - The player who played the card with the highest rank gets a point
            - If there are multiple cards with the same rank, then suits are taken in reverse
              alphabetical order, with SPADES as the highest suit, then HEARTS, then DIAMONDS,
              then CLUBS. The player with the highest suit (among tied-rank cards) gets a point
        - Once any player's hand is empty (or the csv file runs out), the game is over and the
          player with the most points is declared the winner.

    This function should display:
        - The id of the winning player
        - The scores of all players

    The format of the csv file (infile) is as follows:
        - The first row contains the field names:
            - "player"
            - "rank"
            - "suit"
        - Each subsequent row contains, in order:
            - The player id (an integer from 0 to n_players)
            - The name of the rank of the card they played
            - The name of the suit of the card they played
        - The order of the players is the same in each round, and it goes from 0 to n_players
            - That is, the player id repeats the cycle 0, 1, 2, 3, ..., 0, 1, 2, 3, ..., and so on
    """