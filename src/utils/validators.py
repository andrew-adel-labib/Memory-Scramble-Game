from src.utils.exception_handler import (
    InvalidBoardSizeException,
    InvalidTimerException,
)



def validate_board_size(rows, cols):
    if (rows * cols) % 2 != 0:
        raise InvalidBoardSizeException(
            "Board size must be even."
        )

    return True



def validate_timer(seconds):
    if seconds <= 0:
        raise InvalidTimerException(
            "Timer must be greater than zero."
        )

    return True