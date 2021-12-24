if __name__ == '__main__':
    a = int(input())
    b = int(input())


def sum_of_two_numbers(x, y):
    sum_is = x + y
    return sum_is


def difference_of_two_numbers(x, y):
    difference = x - y
    return difference


def product_of_two_numbers(x, y):
    product = x * y
    return product


def main():
    print(sum_of_two_numbers(a, b))
    print(difference_of_two_numbers(a, b))
    print(product_of_two_numbers(a, b))


main()
