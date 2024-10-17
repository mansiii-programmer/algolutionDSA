size = 4
arr = [100, 200, 300, 400]
k = int(input("Enter value of k: "))
windowSum = 0
maxSum = 0

for i in range(k):
    windowSum += arr[i]

maxSum = windowSum

for i in range(1, size - k + 1):
    windowSum = windowSum - arr[i - 1] + arr[i + k - 1]
    if windowSum > maxSum:
        maxSum = windowSum

print(maxSum)
