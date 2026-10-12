dist = float(input())
speed = int(input())
if dist <= 0.1 and speed <= 100:
    print('WIFI')
elif dist <= 10 and speed <= 150:
    print('LTE')
elif dist <= 2 and speed <= 1000:
    print('5G')
elif dist <= 1000 and speed <= 200:
    print('SATELLITE')
else:
    print('бред не вводи')
    