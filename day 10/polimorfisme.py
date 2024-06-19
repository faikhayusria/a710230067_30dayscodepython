class Bird:
    def fly(self):
        return "Bird can fly."

class Penguin(Bird):
    def fly(self):
        return "Penguin can't fly."

# Membuat objek dari kelas Bird dan Penguin
bird1 = Bird()
penguin1 = Penguin()
print(bird1.fly())  # Output: Bird can fly.
print(penguin1.fly())  # Output: Penguin can't fly.
