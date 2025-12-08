class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'Distance {self.distance}')
        print(f'Rate per KM {self.rate_per_km}')
        print(f'Total = {self.fare}')
        print()


def main():
    taxirajd = TaxiRide(4)
    taxirajd.calculate_fare(7)
    taxirajd.print_receipt()
    taxirajd2 = TaxiRide(6)
    taxirajd2.calculate_fare(10)
    taxirajd2.print_receipt()



if __name__ == "__main__":
    main()
