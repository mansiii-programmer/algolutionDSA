size = 6
arr = [7, 1, 5, 3, 6, 4]
profit = 0
minPrice = arr[0]
maxProfit = -1

for i in range(size):
    if minPrice > arr[i]:
        minPrice = arr[i]
    profit = arr[i] - minPrice
    if maxProfit < profit:
        maxProfit = profit

print(maxProfit)
