class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def __init__(self, name, age, color):
        # Super class (init) indicates a class from a main class (Pet)
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Bark")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


p = Pet("Tim", 19)
c = Cat("Bill", 34, "grey")
d = Dog("Monty", 32, "brown")
d.speak()
c.speak()
c.show()
