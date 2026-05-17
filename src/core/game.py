import pygame

from src.core.board import Board
from src.core.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    TITLE,
    DEFAULT_ROWS,
    DEFAULT_COLS,
    DEFAULT_TIME,
)

from src.core.timer import GameTimer

from src.services.asset_loader import (
    load_icons,
    load_font,
)

from src.ui.themes import (
    BACKGROUND_COLOR,
    CARD_BACK_COLOR,
    TEXT_COLOR,
)

from src.utils.logger import logger

class MemoryGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.font = load_font(32)

        self.images = load_icons()

        self.board = Board(
            DEFAULT_ROWS,
            DEFAULT_COLS,
            self.images
        )

        self.timer = GameTimer(DEFAULT_TIME)

        self.running = True

        self.first_card = None
        self.second_card = None

        self.waiting = False
        self.wait_start = 0

        self.moves = 0

    def reset_turn(self):
        self.first_card = None
        self.second_card = None
        
    def handle_click(self, pos):
        if self.waiting:
            return

        card = self.board.get_clicked_card(pos)

        if not card:
            return

        if card.is_flipped or card.is_matched:
            return

        logger.info("Card selected")

        card.is_flipped = True

        if self.first_card is None:
            self.first_card = card

        elif self.second_card is None:
            self.second_card = card

            self.moves += 1

            self.check_match()

    def check_match(self):
        if self.first_card.image == self.second_card.image:
            self.first_card.is_matched = True
            self.second_card.is_matched = True

            logger.info("Match found")

            self.reset_turn()

        else:
            self.waiting = True
            self.wait_start = pygame.time.get_ticks()

    def update(self):
        if self.waiting:
            current = pygame.time.get_ticks()

            if current - self.wait_start > 1000:
                self.first_card.is_flipped = False
                self.second_card.is_flipped = False

                self.reset_turn()

                self.waiting = False
                
    def draw_text(self, text, x, y):
        rendered = self.font.render(
            text,
            True,
            TEXT_COLOR
        )

        self.screen.blit(rendered, (x, y))

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        self.board.draw(
            self.screen,
            CARD_BACK_COLOR
        )

        self.draw_text(
            f"Time: {self.timer.format_time()}",
            40,
            30
        )

        self.draw_text(
            f"Moves: {self.moves}",
            350,
            30
        )
        
        if self.timer.is_time_up():
            self.draw_text(
                "GAME OVER",
                850,
                30
            )

            logger.warning("Game over")

        if self.board.all_matched():
            self.draw_text(
                "YOU WIN!",
                850,
                30
            )

            logger.info("Player won game")

        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.update()
            self.draw()
    
