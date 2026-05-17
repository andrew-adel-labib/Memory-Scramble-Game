import time


class GameTimer:
    def __init__(self, duration):
        self.duration = duration
        self.start_time = time.time()

    def get_remaining_time(self):
        elapsed = time.time() - self.start_time

        remaining = max(
            0,
            self.duration - int(elapsed)
        )

        return remaining

    def is_time_up(self):
        return self.get_remaining_time() <= 0

    def format_time(self):
        remaining = self.get_remaining_time()

        minutes = remaining // 60
        seconds = remaining % 60

        return f"{minutes:02}:{seconds:02}"