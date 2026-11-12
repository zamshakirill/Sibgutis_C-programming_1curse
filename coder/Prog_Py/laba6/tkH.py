n = int(input())
room = []
for _ in range(n):
    p, q = map(int, input().split())
    room.append([p, q])

k = 0
for i in room:
    if i[1] - i[0] >= 2:
        k += 1
print(k)
