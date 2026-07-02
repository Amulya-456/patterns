for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


for i in range(1,6):
    for j in range(1,i + 1):
        print(j, end=" ")
    print()

for i in range(1,6):
    for j in range(1,i + 1):
        print(i, end=" ")
    print()

for i in range(1, 6):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print() 

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(6, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()