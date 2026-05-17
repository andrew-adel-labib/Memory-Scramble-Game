import pygame

from src.ui.themes import (
    BUTTON_COLOR,
    HOVER_COLOR,
)


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        text,
        font,
    ):
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height
        )

        self.text = text
        self.font = font

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()

        color = BUTTON_COLOR

        if self.rect.collidepoint(mouse):
            color = HOVER_COLOR

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=10
        )

        rendered = self.font.render(
            self.text,
            True,
            (255, 255, 255)
        )

        text_rect = rendered.get_rect(
            center=self.rect.center
        )

        screen.blit(rendered, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)