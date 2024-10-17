size = 6
arr = [1, 2, 4, 5, 7, 11]
Sum = int(input("Enter Sum: "))
flag = 0

for i in range(size):
    for j in range(i + 1, size):
        if arr[i] + arr[j] == Sum:
            print("Numbers are:", arr[i], "and", arr[j])
            flag = 1

if flag != 1:
    print("No such numbers found...")
