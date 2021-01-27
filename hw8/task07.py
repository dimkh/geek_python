class ComplexNumber:

    def __init__(self, re=0.0, im=0.0):
        self.re = re
        self.im = im

    def __str__(self):

        if self.im != 0:
            im = f"{self.im}i"
            if self.re != 0 and self.im > 0:        # Есть действительная часть - нужен плюс
                im = f"+{im}"
        else:
            im = ""             # Нулевая мнимая часть не пишется

        if im and self.re == 0:     # При наличии мнимой части нулевая действительная не пишется
            re = ""
        else:
            re = self.re

        return f'{re}{im}'

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return ComplexNumber(re, im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNumber(re, im)


a = ComplexNumber(1, -1)
b = ComplexNumber(3, 6)
print(a+b)
print(a*b)
