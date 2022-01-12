# Given five positive integers, find the minimum and maximum values that can be calculated by
# summing exactly four of the five integers. Then print the respective minimum and maximum values as
# a single line of two space-separated long integers.

# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    s = sum(arr)
    max_val = s - arr[0]
    min_val = s - arr[-1]
    print(min_val, max_val)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)