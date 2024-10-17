arr = [1, 2, 3, 4, 5]
max_value = arr[0]

for num in arr:
    if max_value < num:
        max_value = num

print(max_value)