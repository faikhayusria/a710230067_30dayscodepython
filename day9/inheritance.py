class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Membuat objek dari kelas Cat dan Dog
cat1 = Cat("Whiskers")
dog1 = Dog("Rex")
print(cat1.make_sound())  # Output: Meow
print(dog1.make_sound())  # Output: Bark
