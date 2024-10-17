arr = [1, 2, 4, 3, 3]
frequencyArr = [0] * 5

for i in range(5):
    for j in range(5):
        if arr[i] == arr[j]:
            frequencyArr[i] += 1

for i in range(5):
    if frequencyArr[i] == 1:
        print(arr[i], end="\t")

print()

for i in range(5):
    print(frequencyArr[i], end="\t")

print()

for i in range(5):
    if frequencyArr[i] > 1:
        print(arr[i], end="\t")