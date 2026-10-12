word = input()
s1 = ''
s2 = ''
if word[-1] == "#":
    for i in range(len(word) - 1):
        if i % 2 == 0:
            s1 += word[i]
        else:
            s2 += word[i]
    print(s1 + s2[::-1])
else:
    print("Ошибка! Отсутствует символ #")
