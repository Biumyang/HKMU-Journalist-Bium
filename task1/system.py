from booking import Booking

class BookingSystem:

    def __init__(self):
        self.bookings = []

    def book_flight(self, passenger, flight):

        if flight.seats > 0:

            flight.seats -= 1

            booking = Booking(passenger, flight)

            self.bookings.append(booking)

            booking.confirm()

        else:

            print("No seats available.")