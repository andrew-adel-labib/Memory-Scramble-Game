from src.utils.validators import (
    validate_timer,
)



def test_timer_validation():
    assert validate_timer(60)