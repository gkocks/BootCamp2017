
# solutions.py
"""Volume IB: Testing.
Geoffrey Kocks
June 22, 2017
"""
import math

# Problem 1 Write unit tests for addition().
# Be sure to install pytest-cov in order to see your code coverage change.


def addition(a, b):
    return a + b


def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


# Problem 2 Write unit tests for operator().
def operator(a, b, oper):
    if type(oper) != str:
        raise ValueError("Oper should be a string")
    if len(oper) != 1:
        raise ValueError("Oper should be one character")
    if oper == "+":
        return a + b
    if oper == "/":
        if b == 0:
            raise ValueError("You can't divide by zero!")
        return a/float(b)
    if oper == "-":
        return a-b
    if oper == "*":
        return a*b
    else:
        raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-', abs(self.imag))

# Problem 5: Write code for the Set game here

def test_hand(filename):
    if type(filename) is not str or filename.endswith('.txt') is False:
        raise ValueError("Must submit a valid file name")
    with open(filename, 'r') as input:
        text = input.read
        lines = text.split('\n')
    if len(lines) != 12:
        raise ValueError("Must include exactly 12 cards")
    unique = []
    valid = ["0","1","2"]
    for card in lines:
        if card not in unique:
            unique.append(card)
        if len(card) != 4:
            raise ValueError("Each card must be 4 digits")
        for digit in card:
            if digit not in valid:
                raise ValueError("Each card must be represented in base-3")
    if len(unique) != 12:
        raise ValueError("Cannot include a duplicate card")

    total = 0
    for i in range(10):
        for j in range(i+1, 11):
            for k in range(j+1,12):
                if int(lines[i][0]) + int(lines[j][0]) + int(lines[k][0]) %3 == 0 \
                and int(lines[i][1]) + int(lines[j][1]) + int(lines[k][1]) %3 == 0 \
                and int(lines[i][2]) + int(lines[j][2]) + int(lines[k][2]) %3 == 0 \
                and int(lines[i][3]) + int(lines[j][3]) + int(lines[k][3]) %3 == 0:
                    total += 1
    return total







