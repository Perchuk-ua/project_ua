class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):# ініт це конструктор
        self.brand = brand
        self.passengers = []
    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"B Mashuni {self.brand} taki pasaguru")
            for pasenger in self.passengers:
                print(pasenger.name)
        else:
            print(f"B masuni {self.brand} нema nasaguriv. Bsi Bteklu")

car = Auto("Toyota Supra")
car.add_passenger(Human("Ilur"))
car.add_passenger(Human("Igor"))
car.add_passenger(Human("Maks"))
car.add_passenger(Human("Shasha"))
car.print_passengers()
