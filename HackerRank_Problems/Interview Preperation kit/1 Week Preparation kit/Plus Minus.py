# Problem
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
# though answers with absolute error of up to  are acceptable.

def plusMinus(arr):
    # Write your code here
    pos_num = 0
    neg_num = 0
    zero_num = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_num += 1
        elif arr[i] < 0:
            neg_num += 1
        else:
            zero_num += 1
    print(pos_num / len(arr))
    print(neg_num / len(arr))
    print(zero_num / len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

