class Prova:  # definition
    statico = 'statico'  # static name

    def __init__(self, x) -> None:  # constructor
        super().__init__(x)
        self.x = x  # attribute x
        self.y = self.x * 2

    def method(self):  # method
        return self.x + self.y


print(Prova.statico)  # access static
prova = Prova(1)  # Instantiation
print(prova.method())  # calling a method
print(prova.y)  # accessing attributes

print(prova.__dict__)  # access underling dict
