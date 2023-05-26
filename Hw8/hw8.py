from collections import namedtuple, deque, Counter
from random import random
from typing import Any, Sequence

def uniform(a: float, b: float) -> float:
    """Returns a uniformly-distributed real number in the interval [a, b)."""
    return random()*(b-a)+a

def randrange(start: int, stop: int) -> int:
    """Returns a uniformly distributed integer in the interval [start, stop)."""
    return (random()*(stop-start)+start)//1

def choice(seq: Sequence) -> Any:
    """Returns a randomly-chosen element of `seq`."""
card = namedtuple("Card", "suit rank")

def std_card_deck() -> deque:
    """Returns a deque containing 52 Cards, the standard 52 playing cards."""
    output = deque()
    for i in range(4):
      for j in range(13):
        output.append(card(i,j))
    return output

def riffle_shuffle(deck: deque) -> None:
    """Simulates a 'riffle shuffle' of a deck of cards."""
    deck2=deque()
    totalcards=52
    for i in range(totalcards//2):
      deck2.append(deck.pop)
    deck1=deck
    deck=deque()

    while(len(deck1)!=0 and len(deck2)!=0):
      if(randrange(0,2)//1==0):
        deck.append(deck1.pop)
      else:
        deck.append(deck2.pop)

    

def mix_deck(deck: deque) -> None:
    """Puts deck in a random order."""
    for i in range(len(deck)):
      holder=deck[i]
      randomnumber=randrange(0,len(deck))
      deck[i]=deck[int(randomnumber//1)]
      deck[int(randomnumber//1)]=holder

def deal(deck: deque, n_players: int) -> list:
    """Deals the cards n_players ways."""
    playerlist=[]
    currentplayer=[]
    cardsperplayer=len(deck)//n_players
    for i in range(n_players):
      currentplayer=[]
      for j in range(cardsperplayer):
        currentplayer.append(deck.pop())
      playerlist.append(currentplayer)
    return playerlist

def letter_freq(s: str) -> Counter:
    """Counts the number of times each letter appears in `s`."""
    return Counter(s)

def popular_letter(s: str) -> str:
    """Returns the letter in `s` that appears most often."""

    return letter_freq(s).most_common(1)[0][0]
