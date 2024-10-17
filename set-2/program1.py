def sub_array_largest_sum(arr):
    max_sum = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]
result = sub_array_largest_sum(arr)
print(result)
