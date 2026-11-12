grades = [" 5 ", "неявка", "4", " хор ", "", "100", "2", "два"]
white = []
for i in range(len(grades)):
    grades[i] = grades[i].strip()
for i in grades:
    if i == '2' or i == 'неуд':
        white.append(2)
    elif i == '3' or i == 'уд':
        white.append(3)
    elif i == '4' or i == 'хор':
        white.append(4)
    elif i == '5' or i == 'отл':
        white.append(5)
print(sorted((white[::-1]), reverse=True))