
row = int(input("Enter the row size: "))

# print("1-----------------------------------------------1")
#
# for i in range(row):
#     for j in range(i):
#         print(i, end=" ")
#     print()
#
# print("2-----------------------------------------------2")
#
# for i in range(1, row+1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print()
#
# print("3-----------------------------------------------3")
#
# for i in range(1, row, 1):
#     for j in range(i, row, 1):
#         print(i, end=" ")
#     print()
#
# print("4-----------------------------------------------4")
#
# for i in range(1, row, 1):
#     for j in range(i, row, 1):
#         print(5, end=" ")
#     print()
#
# print("5-----------------------------------------------5")
#
# for i in range(row, 0, -1):
#     for j in range(1, i, 1):
#         print(i-1, end=" ")
#     print()

# print("6-----------------------------------------------6")
#
# for i in range(row, 1, -1):
#     for j in range(0, i, 1):
#         print(j, end=" ")
#     print()
#
# print("6-----------------------------------------------6")
#
# for i in range(1, row, 1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()
#
# print("7-----------------------------------------------7")
#
# for i in range(1, row+1, 1):
#     for j in range(-1+i, -1, -1):
#         print(2**j, end=" ")
#
#     print()

print("8-----------------------------------------------8")

for i in range(1, row, 1):
    for j in range(0, i, 1):
        print(2**j, end=" ")
    for j in range(-i+i, -1, -1):
        print(2**j, end=" ")
    print()

print("8-----------------------------------------------8")




