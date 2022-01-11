# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
stock = list(map(int, input().split(' ')))
dict = Counter(stock)
N = int(input())
p = 0
for i in range(N):
    size, price = map(int, input().split())
    if dict[size]:
        dict[size] -= 1
        p = p + price
print(p)

