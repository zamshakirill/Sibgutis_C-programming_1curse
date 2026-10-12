a = int(input())
b = int(input())
c = int(input())
d = int(input())
def ip(a, b, c, d):
    for i in [a, b, c, d]:
        if i > 255:
            print('INVALID')
            return 0
    if f'{a}.{b}.{c}.{d}' == '127.0.0.1':
        print('LOOPBACK')
    elif f'{a}.{b}.{c}.{d}' == '0.0.0.0':
        print('UNSPECIFIED')
    elif 224 <= a <= 239 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
        print('MULTICAST')
    elif a == 10 or (a == 172 and 16 <= b <= 31) or (a == 192 and b == 168):
        print('PRIVATE')
    else:
        print('PUBLIC')


ip(a, b, c, d)