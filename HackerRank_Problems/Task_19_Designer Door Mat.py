#Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
#Mat size must be N * M (N is an odd natural number, and M is 3 times N.)
#The design should have 'WELCOME' written in the center.
#The design pattern should only use |, . and - characters.


n, m = map(int, input().split())
s1 = '.|.'
s2 = 'welcome'
for i in range(n // 2):
    print((s1 * ((i * 2) + 1)).center(m, '-'))
print(s2.center(m, '-'))
# for i in range(n // 2):
#     print((s1 * ((n-2)-2*i)).center(m, '-'))

for i in range(n // 2 - 1, -1, -1):
    print((s1 * ((i * 2) + 1)).center(m, '-'))
