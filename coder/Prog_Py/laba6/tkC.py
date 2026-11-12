n = input()
h = n.split(' / ')
andrey = int(h[0])
heights = [int(x) for x  in h[1].split()]
pos = sum([1 for x in heights if x >= andrey]) + 1
print(pos)

