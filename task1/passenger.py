class Passenger:

    def __init__(self, name, passport):
        self.name = name
        self.passport = passport

    def display(self):
        print("Passenger:", self.name, "| Passport:", self.passport)