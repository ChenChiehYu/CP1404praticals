from prac_09.musician import Musician
from guitar import Guitar


class Band:
    def __init__(self, name):
        self.name = name
        self.musician = []

    def __str__(self):
        return f"{self.name} ({self.musician})"

    def add(self, musician):
        self.musician.append(musician)

    def play(self):
        for musisicans in self.musician:
            if not musisicans:
                return f"{self.name} needs an instrument!"
            return f"{self.name} is playing: {self.musician[0]}"

