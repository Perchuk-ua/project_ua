class Perchuk:
    def __init__(self, name, list, ):
        self.name = name
        self.list = list
    def average(self):
        print(f"Averege: {sum(self.list) / len(self.list)}")

s1 = Perchuk("Demian", [9, 12, 10, 8 ,5 , 10 , 4 , 7])
s1.average()