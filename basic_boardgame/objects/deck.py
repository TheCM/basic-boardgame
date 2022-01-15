from random import shuffle
from typing import List

from basic_boardgame.objects.card import Card


class Deck:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def __str__(self):
        return [str(card) for card in self.cards]

    def shuffle(self):
        shuffle(self.cards)

    def get_top_card(self):
        return self.cards.pop(0)

    def get_bottom_card(self):
        return self.cards.pop(-1)

    def get_all_cards(self):
        giving_away_cards = self.cards[:]
        self.cards.clear()
        return giving_away_cards

    def place_card_at_bottom(self, card: Card):
        self.cards.append(card)

    def place_cards_at_bottom(self, cards: List[Card]):
        self.cards += cards
