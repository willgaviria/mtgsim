import copy
from typing import List, Optional
import random

from mtgsim.card import Card
import mtgsim.constants as c


class Deck:

    def __init__(
            self,
            spells: int,
            basic_lands: int,
            fetch_lands: Optional[int] = 0):

        self.cards = [Card(type=c.TYPE_SPELL) for _ in range(spells)]
        self.cards += [
            Card(type=c.TYPE_BASIC_LAND) for _ in range(basic_lands)]
        self.cards += [
            Card(type=c.TYPE_FETCH_LAND)for _ in range(fetch_lands)]
        self.shuffle()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, n: Optional[int] = 1) -> List[Card]:
        assert n <= len(self.cards), \
            f'Cannot draw {n} when {len(self.cards)} cards are left in deck.'
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        return copy.deepcopy(drawn)

    def count(self, type: Optional[str] = None) -> int:
        if type:
            count_ls = [c for c in self.cards if c.type == type]

        else:
            count_ls = self.cards

        return len(count_ls)

    def remove(self, type: str) -> Optional[Card]:
        for i, card in enumerate(self.cards):
            if card.type == type:
                return self.cards.pop(i)

    def __len__(self) -> int:
        return len(self.cards)
