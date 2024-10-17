arr = [1, 2, 3, 4, 5]
num = int(input("Enter the number: "))
flag = 0

for i in range(5):
    if arr[i] == num:
        print("Index =", i)
        flag = 1
        break

if flag == 0:
    print(-1)