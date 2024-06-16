class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking."

# Membuat objek dari kelas Dog
dog1 = Dog("Buddy", 3)
print(dog1.bark())  # Output: Buddy is barking.
