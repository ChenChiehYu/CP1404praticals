from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, faciness):
        super().__init__(name, fuel)
        self.faciness = faciness
        self.price_per_km = Taxi.price_per_km*self.faciness

    def get_fare(self):
        return super().get_fare()+self.flagfall

    def __str__(self):
        return f"{Taxi.__str__(self)} plus flagfall of ${self.flagfall:.2f}"