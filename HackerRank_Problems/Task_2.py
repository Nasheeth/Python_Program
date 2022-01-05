# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division, a // b.
# The second line should contain the result of float division, a / b. No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input("a = "))
    b = int(input("b = "))


def integer_division(x, y):
    return x // y


def float_division(x, y):
    return x / y


def main():
    print("The result of the integer division ", a, '//', b, "=", integer_division(a, b))
    print("The result of the float division", a, '/', b, "=", float_division(a, b))


main()
