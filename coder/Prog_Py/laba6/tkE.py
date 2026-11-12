n = input()
treas = [int(x) for x in n.split()]
k = []
ind = []
for i in range(1, len(treas) - 1):
    if treas[i - 1] < treas[i] > treas[i + 1]:
        print(f'Индекс {i}: {treas[i]} > {treas[i - 1]} и {treas[i]} > {treas[i + 1]} => сокровище.')
        k.append(treas[i])
        ind.append(i)
    elif treas[i - 1] > treas[i] > treas[i + 1]:
        print(f'Индекс {i}: {treas[i]} < {treas[i - 1]} и {treas[i]} > {treas[i + 1]} => не сокровище.')
    elif treas[i - 1] < treas[i] < treas[i + 1]:
        print(f'Индекс {i}: {treas[i]} > {treas[i - 1]} и {treas[i]} < {treas[i + 1]} => не сокровище.')
    if treas[i - 1] > treas[i] < treas[i + 1]:
        print(f'Индекс {i}: {treas[i]} < {treas[i - 1]} и {treas[i]} < {treas[i + 1]} => не сокровище.')
if k:
    print('Сокровища на индексах', *ind, 'со значениями', *k)
    print('Самое глубокое -', max(k))
    treas.remove(max(k))
    print(f'Удаляем первое вхождение числа {max(k)} из списка:')
print(treas, '- это и есть ответ.')
