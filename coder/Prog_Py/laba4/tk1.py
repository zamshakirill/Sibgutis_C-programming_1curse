a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
l = max(a1, b1)
r = min(a2, b2)
if l < r:
    print(f'[{l},{r}], длина {r - l}')
elif l == r:
    print(f'точка {r}, длина {r - l}')
else:
    print('Пересечений нет')
