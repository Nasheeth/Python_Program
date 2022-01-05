# The provided code stub reads and integer,n, from STDIN. For all non-negative integers i < n, print i**2.

if __name__ == '__main__':
    n = int(input("n = 3"))


def power_of(x):
    a = x * x
    return a


def main():
    for i in range(n):
        print(power_of(i))


main()
