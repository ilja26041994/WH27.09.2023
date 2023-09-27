# Создать класс Triangle с полями-сторонами. Определить методы изменения
# сторон, вычисления углов, вычисления периметра. Создать производный
# класс Equilateral (равносторонний), имеющий поле площади. Определить
# метод вычисления площади.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def change_side(self, new_a, new_b, new_c):
        self.a = new_a
        self.b = new_b
        self.c = new_c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

class Equilateral(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)

    def area(self):
        areA = (self.a ** 2 * 3**0.5) / 4
        return areA

side = Triangle(3, 4, 5)
print(side.perimeter())
print(side.area())
print(side.a)
print(side.b)
print(side.c)
side.change_side(4, 5, 6)
print(side.a)
print(side.b)
print(side.c)
print(side.perimeter())
print(side.area())

sideEquilateral = Equilateral(3)
print(sideEquilateral.area())
