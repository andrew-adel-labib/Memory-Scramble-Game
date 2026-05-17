import os
import pygame

from src.utils.logger import logger
from src.utils.exception_handler import (
    AssetLoadingException,
)

ICON_PATH = "assets/icons"
FONT_PATH = "assets/fonts/Poppins-Regular.ttf"


def load_icons():
    images = []

    try:
        for file in os.listdir(ICON_PATH):
            if file.endswith(".png"):
                path = os.path.join(ICON_PATH, file)

                image = pygame.image.load(path).convert_alpha()

                images.append(image)

        logger.info("Icons loaded successfully")

        return images

    except Exception as error:
        raise AssetLoadingException(f"Failed to load icons: {error}")


def load_font(size):
    try:
        logger.info("Font loaded successfully")

        return pygame.font.Font(FONT_PATH, size)

    except Exception as error:
        raise AssetLoadingException(f"Failed to load font: {error}")
