columns = int(input())

for i in range(columns):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(columns, -1, -1):
    for j in range(i - 1, 0, -1):
        print("*", end="")
    print()
