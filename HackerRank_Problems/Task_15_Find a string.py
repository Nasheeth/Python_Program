# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    # c = 0
    # length = len(sub_string)
    # for i in range(len(string)):
    #     s = string[i:i + length]
    #     if s == sub_string:
    #         c += 1
    # return c

#using find function

    c = 0
    x = -1
    while x < len(string):
        s = string.find(sub_string, x+1)
        if s == -1:
            break
        c += 1
        x = s
    return c




if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
