class Flight:

    def __init__(self, flight_no, origin, destination, seats):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.seats = seats

    def display(self):
        print("Flight:", self.flight_no)
        print("Route:", self.origin, "->", self.destination)
        print("Seats left:", self.seats)