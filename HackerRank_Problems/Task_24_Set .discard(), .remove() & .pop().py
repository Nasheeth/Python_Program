# You have a non-empty set s, and you have to execute N commands given in N lines.
# The commands will be pop, remove and discard.

n = int(input())
s = set(map(int, input().split()))
cm = int(input())
for i in range(cm):
    s1 = list(input().split())
    if s1[0] == "pop":
        s.pop()
    elif s1[0] == "remove":
        s.remove(int(s1[1]))
    elif s1[0] == "discard":
        s.discard(int(s1[1]))
# print(s)
sum1 = 0
for i in s:
    sum1 = sum1 + i
print(sum1)