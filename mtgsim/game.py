from typing import Optional

from mtgsim.deck import Deck
from mtgsim.hand import Hand
import mtgsim.constants as c


class Game:

    def __init__(self,
                 deck: Deck,
                 start_hand_size: Optional[int] = c.START_HAND_SIZE,
                 start_on_play: Optional[bool] = True,
                 verbose: Optional[bool] = False):
        self.deck = deck
        self.hand = Hand()
        self.hand.add(self.deck.draw(start_hand_size))
        self.board = []
        self.life = c.START_LIFE
        self.start_on_play = start_on_play
        self.verbose = verbose
        self.turn = 0

        # Stats
        self.missed_land_drop_turn = []

        if verbose:
            print(f'On the play: {self.start_on_play}')
            print(f'Starting life: {self.life}')
            print(f'Starting hand size: {len(self.hand)}')
            print(f'Starting hand: {self.hand.cards}')

    def play_turn(self):
        self.turn += 1

        if self.verbose:
            print(f'-- Turn {self.turn} (cards left: {len(self.deck)})')

        # Draw step
        if self.start_on_play and self.turn == 0:
            pass
        else:
            self.hand.add(self.deck.draw())

        # Get land to play
        if self.deck.count(type=c.TYPE_BASIC_LAND) == 0:
            land = self.hand.remove_basic_land()
        else:
            land = self.hand.remove_land()

        # If no land to play, record land drop
        if land is None:
            if self.verbose:
                print(f'---- Missed land drop (hand: {self.hand.cards}')
            self.missed_land_drop_turn.append(self.turn)

        # Otherwise, play the land
        else:

            # Fetch if necessary
            if land.type == c.TYPE_FETCH_LAND:
                self.life -= 1
                land = self.deck.remove(type=c.TYPE_BASIC_LAND)
                self.deck.shuffle()
                if self.verbose:
                    print('---- Fetched land')

            # Play the land
            self.board.append(land)
            if self.verbose:
                print('---- Played land')
