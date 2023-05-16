class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, human):
        if len(self.passengers) < self.capacity:
            self.passengers.append(human)
        else:
            print(f"А шо ти?Ти зайвий")

    def print_passengers(self):
        if self.passengers:
            print(f"В машині {self.brand} такі пасажири:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"В машині {self.brand} немає пасажирів. Всі втікли!")


car = Auto('Nissan GTR', 4)
car.add_passenger(Human("Oleg"))
car.add_passenger(Human("Igor"))
car.add_passenger(Human("Vlad"))
car.add_passenger(Human("Valentyn"))
car.add_passenger(Human("Valentyn"))
car.print_passengers()
