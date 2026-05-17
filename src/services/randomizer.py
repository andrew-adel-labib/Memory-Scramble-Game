import random


class Randomizer:
    @staticmethod
    def shuffle(items):
        random.shuffle(items)
        return items
