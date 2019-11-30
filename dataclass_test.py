# coding: utf-8
# @Time: 2019-07-24 17:57
# @Author: 'haifeng.shi@klook.com'

from dataclasses import dataclass, field
from typing import List

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory= make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


queen_of_hearts=PlayingCard('Q', 'Hearts')
ace_of_spades=PlayingCard('A', 'Spades')
print(ace_of_spades)
two_cards=Deck([queen_of_hearts, ace_of_spades])
print(two_cards)
print(Deck())


@dataclass(frozen=True)
class Position:
    name: str
    lon: float=0.0
    lat: float=0.0



