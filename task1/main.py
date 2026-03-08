from passenger import Passenger
from flight import Flight
from system import BookingSystem


def main():

    passenger1 = Passenger("Alice", "P123456")

    flight1 = Flight("CX101", "Hong Kong", "Tokyo", 2)

    system = BookingSystem()

    system.book_flight(passenger1, flight1)

    flight1.display()


if __name__ == "__main__":
    main()