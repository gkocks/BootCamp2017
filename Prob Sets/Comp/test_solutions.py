# test_solutions.py
"""Volume 1B: Testing.
    <Name>
    <Class>
    <Date>
    """

import solutions as soln
import pytest
import math

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1.2, 2.3) == 3.5, "Addition failed on positive floats"
    assert soln.addition(3,5) == 8, "Addition failed on positive integers"
    assert soln.addition(-3,-4) == -7, "Addition failed on negative integers"
    assert soln.addition(-2.3, -1.2) == -3.5, "Addition failed on negative floats"
    assert soln.addition(-1, 2) == 1

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1
    assert soln.smallest_factor(3) == 3
    assert soln.smallest_factor(25) == 5

# Problem 2: Test the operator function from solutions.py
def test_operator():
    assert soln.operator(2,3,"+") == 5
    assert soln.operator(4,2,"/") == 2
    assert soln.operator(5,3,"-") == 2
    assert soln.operator(3,2,"*") == 6
    with pytest.raises(Exception) as exc1:
        soln.operator(2,3,3)
    assert exc1.typename == "ValueError"
    assert exc1.value.args[0] == "Oper should be a string"
    with pytest.raises(Exception) as exc2:
        soln.operator(2,3,"+*")
    assert exc2.typename == "ValueError"
    assert exc2.value.args[0] == "Oper should be one character"
    with pytest.raises(Exception) as exc3:
        soln.operator(2,0,"/")
    assert exc3.typename == "ValueError"
    assert exc3.value.args[0] == "You can't divide by zero!"
    with pytest.raises(Exception) as exc4:
        soln.operator(2,3,"&")
    assert exc4.typename == "ValueError"
    assert exc4.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

def test_complex_subtraction(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 - number_2 == soln.ComplexNumber(-4, -3)
    assert number_1 - number_3 == soln.ComplexNumber(-1, -7)
    assert number_2 - number_3 == soln.ComplexNumber(3, -4)
    assert number_3 - number_3 == soln.ComplexNumber(0, 0)

def test_complex_division(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 / number_2 == soln.ComplexNumber(0.3, 0.1)
    assert number_1 / number_3 == soln.ComplexNumber(4/17, -1/17)
    assert number_2 / number_3 == soln.ComplexNumber(11/17, -7/17)
    assert number_3 / number_3 == soln.ComplexNumber(1, 0)
    with pytest.raises(Exception) as exc:
        number_1/soln.ComplexNumber(0,0)
    assert exc.typename=="ValueError"
    assert exc.value.args[0] == "Cannot divide by zero"

def test_equals(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert (number_1 == soln.ComplexNumber(1,2)) == True
    assert (number_1 == soln.ComplexNumber(1,3)) == False

def test_norm(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_2.norm() == math.sqrt(50)

def test_complex_print(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert str(number_1) == "1+2i"

# Problem 4: Write test cases for the Set game.
def test_hand():
    with pytest.raises(Exception) as exc1:
        soln.test_hand("hand1.txt")
    assert exc1.typename == "ValueError"
    assert exc1.value.args[0] == "Must include exactly 12 cards"

    with pytest.raises(Exception) as exc2:
        soln.test_hand("hand2.txt")
    assert exc2.typename == "ValueError"
    assert exc2.value.args[0] == "Cannot include a duplicate card"

    with pytest.raises(Exception) as exc2a:
        soln.test_hand("hand2a.pdf")
    assert exc2a.typename == "ValueError"
    assert exc2a.value.args[0] == "Must submit a valid file name"

    with pytest.raises(Exception) as exc3:
        soln.test_hand("hand3.txt")
    assert exc3.typename == "ValueError"
    assert exc3.value.args[0] == "Each card must be 4 digits"

    with pytest.raises(Exception) as exc4:
        soln.test_hand("hand4.txt")
    assert exc4.typename == "ValueError"
    assert exc4.value.args[0] == "Each card must be represented in base-3"





