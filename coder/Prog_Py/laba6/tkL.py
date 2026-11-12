n, q = map(int, input().split())
l = []
for i in range(1, n + 1):
    l.append(i)

k = []
newl = []
while len(l) != 1:
    if len(l) < q:
        k.append(l.pop(q - (len(l) - 1) - len(l)))
        l = l[q - (len(l)- 1) - len(l):] + l[:q - (len(l) - 1) - len(l)]
    else:    
        k.append(l.pop(q - 1))
        l = l[q - 1:] + l[:q - 1]

print(*k, '\n', *l)
