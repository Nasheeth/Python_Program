# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11

# >>> from collections import namedtuple
# >>> Car = namedtuple('Car','Price Mileage Colour Class')
# >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# >>> print xyz
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# >>> print xyz.Class
# Y


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
from collections import namedtuple
data = namedtuple("data",input())
print(sum([int(data(*input().split()).MARKS) for i in range(N)])/N)


# N = int(input())
# from collections import namedtuple
# data = namedtuple("data",input())
# mark_lst = []
# for i in range(N):
#     marks = int(data(*input().split()).MARKS)
#     mark_lst.append(marks)
# print(sum(mark_lst)/N)
