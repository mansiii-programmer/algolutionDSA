size = 6
arr = [1, 2, 4, 5, 7, 11]
Sum = int(input("Enter Sum: "))
flag = 0

i = 0
j = size - 1
while i < j:
    if arr[i] + arr[j] > Sum:
        j -= 1
    elif arr[i] + arr[j] < Sum:
        i += 1
    else:
        print("Numbers are:", arr[i], "and", arr[j])
        flag = 1
        i += 1
        j -= 1

if flag != 1:
    print("No such numbers found...")
