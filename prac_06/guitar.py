YEAR = 2023


class Guitar:
    def __init__(self, name, year, cost):
        self.name = ""
        self.year = 0
        self.cost = float(0.0)
        self.name = name
        self.year = year
        self.cost = float(cost)

    def __str__(self):
        return f"{self.name} ({self.year}) : ${float(self.cost):10,.2f}"

    def get_age(self):
        age = YEAR - int(self.year)
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
