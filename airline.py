class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if self.open_seats() <= 0:
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)


people = ["a", "b", "c", "d", "e", "f", "g"]
for i in people:
    success = flight.add_passanger(i)
    if success:
        print("added")
    else:
        print("not added")
