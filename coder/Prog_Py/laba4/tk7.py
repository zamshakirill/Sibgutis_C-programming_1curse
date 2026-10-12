a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a and d:
    print('CLOSED')
elif (a and not b) or (c and d):
    print('OPEN')
else:
    print('CLOSED')
    