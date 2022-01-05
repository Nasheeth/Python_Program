def swap_case(s):
    k = ""
    for c in s:
        if c.isupper():
            c = c.lower()
        else:
            c = c.upper()
        k += "".join(c)
    return k


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
