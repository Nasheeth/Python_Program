# You are given a string S.
# Your task is to print all possible permutations of size K of the string in lexicographic sorted order.
from itertools import permutations

S, K = input().split(' ')
for i in tuple(permutations(sorted(S), int(K))):
    print(''.join(i))