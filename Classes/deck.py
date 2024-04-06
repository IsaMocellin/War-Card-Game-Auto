import random
from .card import Card

class Deck:
    def __init__(self, values):
        self.all_cards = []
        self.values = values
        self.suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
        self.ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 'Jack', 'Queen', "King", "Ace"}
        self.generate_deck()

    def generate_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                created_card = Card(suit, rank, self.values)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
