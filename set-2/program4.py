size = 7
arr = [-7, 1, 5, 2, -4, 3, 0]
flag = 0

for i in range(size):
    leftSum = 0
    rightSum = 0
    for j in range(size):
        if i > j:
            leftSum += arr[j]
        elif i < j:
            rightSum += arr[j]
    if leftSum == rightSum:
        print("Equilibrium Index =", i)
        flag = 1

if flag == 0:
    print(-1)