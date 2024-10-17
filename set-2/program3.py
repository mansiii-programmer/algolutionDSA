str = "A man, a plan, a canal: Panama"
strCpy = ""

for c in str:
    c = c.lower()
    if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
        strCpy += c

flag = 0
n = len(strCpy)

for i in range(len(strCpy)):
    n -= 1
    if strCpy[i] != strCpy[n]:
        flag = 0
        break
    flag = 1

if flag == 1:
    print("Palindrome")
else:
    print("Not a Palindrome")
