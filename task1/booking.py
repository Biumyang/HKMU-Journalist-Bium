class Booking:

    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def confirm(self):
        print("Booking confirmed!")
        print(self.passenger.name, "booked flight", self.flight.flight_no)