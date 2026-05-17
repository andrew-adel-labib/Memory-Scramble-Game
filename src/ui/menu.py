import pygame

from src.ui.button import Button
from src.ui.themes import BACKGROUND_COLOR


class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font

        self.start_button = Button(
            450,
            300,
            300,
            80,
            "Start Game",
            font
        )

    def run(self):
        running = True

        while running:
            self.screen.fill(BACKGROUND_COLOR)

            self.start_button.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.is_clicked(event.pos):
                        return True