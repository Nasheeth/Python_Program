a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

if a >= b and a >= c:
    print(a + " is largest")
elif b >= a and b >= c:
    print(b + " is largest")
else:
    print(c + " is largest")
