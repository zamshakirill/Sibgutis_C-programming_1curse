n = int(input())
def arm(n):
    s = str(n)
    count = 0
    while n != 0:
        count += (n % 10)**len(s)
        n = n // 10
    if s == str(count):
        return 1
    else:
        return 0

    
k = 0
for i in range(1, n + 1):
    if arm(i):
        k += 1
print(k)