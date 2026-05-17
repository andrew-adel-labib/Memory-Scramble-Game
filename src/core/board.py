import random

from src.core.card import Card
from src.core.constants import (
    CARD_SIZE,
    CARD_MARGIN,
)


class Board:
    def __init__(self, rows, cols, images):
        self.rows = rows
        self.cols = cols
        self.images = images

        self.cards = []

        self.generate_cards()

    def generate_cards(self):
        needed_pairs = (
            self.rows * self.cols
        ) // 2

        selected = self.images[:needed_pairs]

        card_images = selected * 2

        random.shuffle(card_images)

        self.cards.clear()

        start_x = 150
        start_y = 120

        index = 0

        for row in range(self.rows):
            for col in range(self.cols):
                x = start_x + col * (
                    CARD_SIZE + CARD_MARGIN
                )

                y = start_y + row * (
                    CARD_SIZE + CARD_MARGIN
                )

                card = Card(
                    card_images[index],
                    x,
                    y,
                    CARD_SIZE
                )

                self.cards.append(card)

                index += 1

    def draw(self, screen, back_color):
        for card in self.cards:
            card.draw(screen, back_color)

    def get_clicked_card(self, pos):
        for card in self.cards:
            if card.contains(pos):
                return card

        return None

    def all_matched(self):
        return all(
            card.is_matched
            for card in self.cards
        )