# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where k not equal to 1
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Anant has an unordered list of randomly arranged room entries.
# The list consists of the room numbers for all of the tourists.
# The room numbers will appear K times per group except for the Captain's room.
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of K and the room number list.

k = int(input())
lst = list(map(int, input().split()))
s1 = set()
s2 = set()
for i in lst:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s = s1.difference(s2)
print(*s)





