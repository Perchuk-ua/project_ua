class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age}")


class Employee(Person):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def display_details(self):
        super().say_hello()
        print(f"Salary: {self.salary}")
        print(f"Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, age, gender, salary, position, num_subordinates):
        super().__init__(name, age, gender, salary, position)
        self.num_subordinates = num_subordinates

    def display_details(self):
        super().display_details()
        print(f"Number of Subordinates: {self.num_subordinates}")


class Developer(Employee):
    def __init__(self, name, age, gender, salary, position, programming_language):
        super().__init__(name, age, gender, salary, position)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")


# Приклад використання класів
e = Employee("John", 30, "Male", 5000, "Employee")
e.display_details()

m1 = Manager("Smith", 35, "Female", 8000, "Manager", 15)
m1.display_details()

d1 = Developer("Mike", 28, "Male", 6000, "Developer", "Python")
d1.display_details()
