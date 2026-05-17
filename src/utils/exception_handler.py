from src.utils.logger import logger


class GameException(Exception):
    pass


class InvalidBoardSizeException(GameException):
    pass


class AssetLoadingException(GameException):
    pass


class InvalidTimerException(GameException):
    pass



def handle_exception(error):
    logger.error(str(error))