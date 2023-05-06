# class Human:
#     height = 180
#
# class Student(Human):
#     pass
#
# class Worker(Human):
#     pass
#
# s1 = Student()
# w1 = Worker()
# print(s1.height)
# print(w1.height)

# class Human:
#     def __init__(self):
#         print("hello, мир, ")
#
#
# class Student(Human):
#     def __init__(self):
#         super().__init__()
#         print("Манера крутит мир")
#
# a = Student()

# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# a = Class2()



# class Animal:
#     def __init__(self, name, age , species):
#         self.name = name
#         self.age = age
#         self.species = species
#
#         def make_sound(self):
#             print('The animal makes a sound!')
#
# class Dog(Animal):
#     def __init__(self, name , age):
#         super().__init__(name, age, species="dog")
#
#     def make_sound(self):
#         print("Woof")
#
# class Cat(Animal):
#     def __init__(self, name , age):
#         super().__init__(name, age, species="cat")
#
#     def make_sound(self):
#         print("Meow")
#
# cat = Cat("Fluffy", 2)
# dog = Dog("Buddy", 4)
#
# print(cat.name)
# print(cat.species)
#
# print(dog.name)
# print(dog.species)
#
# cat.make_sound()
# dog.make_sound()






class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age}")
class Student(Person):
        def __init__(self, name, age, gender, student_id):
            super().__init__(name, age, gender)
            self.student_id = student_id

            def say_hello(self):
                print(f"Hello, my name is {name} and my student ID is {student_id}")

class Teacher(Person):
    def __init__(self, name, age, gender,subject):
        super().__init__(name, age, gender)
        self.subject = subject

        def say_hello(self):
            print(f"Hello, my name is {name} and my student ID is {self.subject}")



class Engineer(Person):
    def __init__(self, name, age, gender , company):
        super().__init__(name, age, gender)
        self.company = company

        def say_hello(self):
            print(f"Hello, my name is {name} and my student ID is {self.company}")

s1 = Student("Dino", 22 , "Male", "1808")
t1 = Teacher("Ann", 32 , "Female", "IT")
e1 = Engineer("Misha", 43 , "Male", "It Step Compani")

s1.say_hello()
t1.say_hello()
e1.say_hello()

