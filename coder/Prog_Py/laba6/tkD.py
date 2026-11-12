from random import choice

oreshka = []
k, c  = 0, 0
while k < 1:
    op = choice(['O', 'P'])
    oreshka.append(op)
    c += 1
    if len(oreshka) >= 3 and oreshka[-1] == oreshka[-2] == oreshka[-3]:
        k += 1
print(*oreshka, f'(попыток: {c})')
