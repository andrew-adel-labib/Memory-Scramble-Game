import pygame


class Card:
    def __init__(self, image, x, y, size):
        self.image = image

        self.rect = pygame.Rect(
            x,
            y,
            size,
            size
        )

        self.is_flipped = False
        self.is_matched = False

    def draw(self, screen, back_color):
        if self.is_flipped or self.is_matched:
            scaled = pygame.transform.scale(
                self.image,
                (self.rect.width, self.rect.height)
            )

            screen.blit(scaled, self.rect)

        else:
            pygame.draw.rect(
                screen,
                back_color,
                self.rect,
                border_radius=12
            )

    def contains(self, pos):
        return self.rect.collidepoint(pos)