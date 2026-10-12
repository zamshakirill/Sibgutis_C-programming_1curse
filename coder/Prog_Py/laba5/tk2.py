n = int(input())
k = 1
for i in range(1, n + 1):
    s = '#' * k
    p = ' ' * (n - i)
    print(f'{p}{s}')
    k += 2
print(f'{' ' * (n - 1)}#')