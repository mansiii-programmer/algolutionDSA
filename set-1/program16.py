def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end="")
        for j in range(n + 1, n + (i - 1) + 1):
            print(n, end="")
        print()

n = 5
print_pattern(n)            
