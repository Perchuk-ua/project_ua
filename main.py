class Perchuk:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def info(self):
        print(f"Student: {self.name} {self.surname}")
    def massage(self, text):
        print(f"Слава Україні, {self.name}. {text}")
s1 = Perchuk("Demian", "Barabash", 35)
s2 = Perchuk("ilur", "ilurovich", 25)
s1.info()
s2.info()
s1.massage("Героям Слава")