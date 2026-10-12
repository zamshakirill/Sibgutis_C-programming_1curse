from random import randint

n = randint(1, 100)
while True:
    number = int(input())
    if number > n:
        print('Меньше')
    elif number < n:
        print('Больше')
    else:
        print('Угадал!')
        break
