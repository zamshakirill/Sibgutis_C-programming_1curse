minutes = int(input())
hour = int(input())
if 0 <= hour <= 5 and 22 <= hour <= 23:
    if minutes <= 30:
        print('0 p') 
    elif 30 < minutes <= 120:
        print(f'{int(100 + 100*0.2)} p')
    elif 120 < minutes <= 300:
        print(f'{int(250 + 250*0.2)} p')
    else:
        print(f'{int(500 + 500*0.2)} p')
else:
    if minutes <= 30:
        print('0 p') 
    elif 30 < minutes <= 120:
        print(f'{100} p')
    elif 120 < minutes <= 300:
        print(f'{250} p')
    else:
        print(f'{500} p')
        