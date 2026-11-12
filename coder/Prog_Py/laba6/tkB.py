n = input()
sell = n.split()
k = []
for i in range(len(sell) - 1):
    if sell[i] < sell[i + 1]:
        k.append(sell[i + 1])
print(*k)