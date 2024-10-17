arr = [0] * 7
n = 6

for i in range(7):
    arr[i] = int(input())

for i in range(3):
    if i >= n:
        break
    arr[i], arr[i + n] = arr[i + n], arr[i]
    n -= 1

for i in range(7):
    print(arr[i], end=" ")
