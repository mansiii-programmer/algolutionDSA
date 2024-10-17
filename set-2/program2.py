def count_inversions(arr):
    count_inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count_inversions += 1
                
    return count_inversions

arr = [7, 2, 6, 3]
result = count_inversions(arr)
print(result)
