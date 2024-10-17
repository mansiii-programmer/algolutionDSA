arr1 = [1, 2, 3, 4, 5]
arr2 = [-5, 6, -3, -2, -1]
arr3 = [0] * 10  
count = 0
i = 0
j = 0

for k in range(10):
    if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
        arr3[k] = arr1[i]
        i += 1
    else:
        arr3[k] = arr2[j]
        j += 1

    print(arr3[k], end="\t")