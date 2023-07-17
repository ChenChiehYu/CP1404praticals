"""
CP1404/CP5632 - Practical
for loops
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
stars=int(input("Number of stars: "))
for i in range(stars):
    print("*", end='')
print()
stars=int(input("Number of stars: "))
for i in range(stars):
    for j in range(i+1):
        print("*", end='')
    print()