import pygame

from src.core.game import MemoryGame
from src.utils.logger import logger
from src.utils.exception_handler import handle_exception


def main():
    try:
        pygame.init()

        logger.info("Game started")

        game = MemoryGame()
        game.run()

        pygame.quit()

        logger.info("Game closed")

    except Exception as error:
        handle_exception(error)


if __name__ == "__main__":
    main()
