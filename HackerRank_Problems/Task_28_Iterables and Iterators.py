# The input consists of three lines. The first line contains the integer N,
# denoting the length of the list. The next line consists of N space-separated lowercase English letters,
# denoting the elements of the list.The third and the last line of input contains the integer K,
# denoting the number of indices to be selected.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
a = int(input())
s = input().split(' ')
k = int(input())

c = 0
for i in combinations(s, k):
    if 'a' in i:
        c = c + 1
print(c / (len(list(combinations(s, k)))))