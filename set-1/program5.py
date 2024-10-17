arr = [1, 2, 1, 2, 1]
n = 4
flag = 0

for i in range(2):
    if arr[i] != arr[n]:
        flag = 0
        break
    n -= 1
    flag = 1

if flag == 1:
    print("Palindrome")
else:
    print("Not a Palindrome")
