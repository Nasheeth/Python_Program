# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s) having the second-lowest grade.
# Note: If there are multiple students with the second-lowest grade,
# order their names alphabetically and print each name on a new line.

n = int(input())
grade = []
result = []
for i in range(n):
    name = input()
    mark = float(input())
    result.append([name, mark])
    grade.append(mark)
print(result)
print(grade)
grade = sorted(set(grade))
print(grade)
m = grade[1]
print(m)
name = []
for val in result:
    if m == val[1]:
        name.append(val[0])
print(name)
name.sort()
for j in name:
    print(j)
