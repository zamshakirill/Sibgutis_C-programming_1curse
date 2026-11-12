card = input()
digits = [int(x) for x in card]
even = []
odd = []
for i in range(len(digits)):
    if i % 2 != 0:
        even.append(digits[i])
    else:
        odd.append(digits[i])
if sum(odd) * 2 > 9:
    summ = (sum(odd) * 2 - 9) + sum(even)
else:
    summ = (sum(odd) * 2) + sum(even)

if summ % 10 == 0:
    print('Корректный номер')
else:
    print('Некорректный номер')