import copy
from typing import List, Optional

from mtgsim.deck import Deck
from mtgsim.game import Game
import mtgsim.constants as c


def simulate(n_games: int,
             spells: int,
             basic_lands: int,
             turns_to_record: List[int],
             fetch_lands: Optional[int] = 0,
             verbose: Optional[bool] = False
             ) -> None:

    # Initialize stats counter
    turn_stats = {t: {} for t in turns_to_record}
    for k in turn_stats.keys():
        turn_stats[k]['mana_on_board'] = []
        turn_stats[k]['fetch_prob'] = []
        turn_stats[k]['basic_prob'] = []
        turn_stats[k]['spell_prob'] = []
        turn_stats[k]['life_burn'] = []
        turn_stats[k]['missed_land_drops'] = []

    deck = Deck(
        spells=spells, basic_lands=basic_lands, fetch_lands=fetch_lands)
    for _ in range(n_games):
        game = Game(deck=copy.deepcopy(deck), verbose=verbose)
        game.deck.shuffle()

        for i in range(max(turn_stats.keys())):
            game.play_turn()

            if game.turn in turn_stats.keys():

                total_cards = game.deck.count()
                fetches = game.deck.count(type=c.TYPE_FETCH_LAND)
                basics = game.deck.count(type=c.TYPE_BASIC_LAND)
                spells = total_cards - fetches - basics

                turn_stats[game.turn]['mana_on_board'] += [len(game.board)]
                turn_stats[game.turn]['fetch_prob'] += [
                    100 * fetches / total_cards]
                turn_stats[game.turn]['basic_prob'] += [
                    100 * basics / total_cards]
                turn_stats[game.turn]['spell_prob'] += [
                    100 * spells / total_cards]
                turn_stats[game.turn]['life_burn'] += [
                    c.START_LIFE - game.life]
                turn_stats[game.turn]['missed_land_drops'] += [
                    len(game.missed_land_drop_turn)]

    for k in turn_stats.keys():
        print(f'Turn {k} stats:')
        results = turn_stats[k]

        for k, v in results.items():
            print(f'Avg. {k}: {(sum(v)/len(v)):.2f}')
        print()
