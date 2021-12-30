#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    l1 = len(first)
    l2 = len(last)
    if l1 <= 10 and l2 <= 10:
    # print("Hello " + first + " " + last + "! " + "You just delved into python.")
        print("Hello {0} {1}! You just delved into python.".format(first, last))
    else:
        print("Given string length is greater than 10")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)