from src.utils.validators import (
    validate_board_size,
)



def test_board_size_validation():
    assert validate_board_size(4, 4)