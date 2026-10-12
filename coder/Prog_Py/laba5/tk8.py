line1 = input()
line2 = input()
line3 = input()
slog = "аеёиоуыэюя"
def haiku(s):
    k = 0
    for i in s:
        if i.lower() in slog:
            k += 1
    return k

if line1 == '' or line2 == '' or line3 == '':
    print("Не хайку. Должно быть 3 строки.")
elif haiku(line1) == 5 and haiku(line2) == 7 and haiku(line3) == 5:
    print("Хайку!")
else:
    print("Не хайку.")
