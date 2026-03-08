class Heap:

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def display(self):
        print(self.data)