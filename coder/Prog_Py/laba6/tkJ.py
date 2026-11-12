n, q = map(int, input().split())
l = list(map(int, input().split()))
if len(l) > n:
    print('Некорректный ввод')
k = [0] * n
for i in range(n):
    k[i - (n - q)] = l[i]
print(*k)