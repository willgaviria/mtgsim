from typing import List, Optional

import mtgsim.constants as c
from mtgsim.card import Card

land_types = [c.TYPE_BASIC_LAND, c.TYPE_FETCH_LAND]


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, cards: List[Card]) -> None:
        self.cards += cards

    def remove_land(self) -> Optional[Card]:
        basic_lands = [
            i for i, card in enumerate(self.cards)
            if card.type == c.TYPE_BASIC_LAND
        ]
        fetch_lands = [
            i for i, card in enumerate(self.cards)
            if card.type == c.TYPE_FETCH_LAND
        ]

        if len(fetch_lands) > 0:
            land = fetch_lands[0]

        elif len(basic_lands) > 0:
            land = basic_lands[0]

        else:
            return None

        return self.cards.pop(land)

    def remove_basic_land(self) -> Optional[Card]:
        basic_lands = [
            i for i, card in enumerate(self.cards)
            if card.type == c.TYPE_BASIC_LAND
        ]

        if len(basic_lands) > 0:
            land = basic_lands[0]

        else:
            return None

        return self.cards.pop(land)

    def __len__(self) -> int:
        return len(self.cards)
