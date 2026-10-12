massage = input('Введите сообщение: ')

def poli(s):
    st = ''
    for i in s:
        if i.isalpha():
            st += i
    if st.lower() == st[::-1].lower():
        return 'Это полиндром'
    else:
        return 'Это не полиндром'

    
def gl(s):
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('A') + s.count('E') + s.count('I') + s.count('O') + s.count('U')


def digit(s):
    if s.isdigit():
        return 'Здесь только цифры'
    else:
        return 'Здесь не только цифры'


def alpha(s):
    if s.isalpha():
        return 'Здесь только буквы'
    else:
        return 'Здесь не только буквы'

def pov(s):
    return s[::-1]


def p_(s):
    return s.replace(' ', '_')


def isemail(s):
    war = '!#$ %&^<>,?;()=}*:/{[]`~|аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ'
    for i in war:
        if i in s:
            return 'Это не email'
    if s.count('@') == 1 and s[0] != '.':
        dog = s.find('@')
        name = s[:dog + 1]
        postname = s[dog + 1:]
        if name[-1] != '.' and postname[0] != '.':
            postname.replace('..', '*')
            if not('*' in postname):
                return 'Это email' 
    else:
        return 'Это не email'


def domen(s):
    if isemail(s) == 'Это email':
        return s[s.find('@'):]
    else:
        return 'Это не email'


while True:
    number = int(input('Выберите действие (1-11): '))
    match number:
        case 1:
            print(poli(massage))
        case 2:
            print(gl(massage))
        case 3:
            print(digit(massage))
        case 4:
            print(alpha(massage))
        case 5:
            print(pov(massage))
        case 6:
            print(massage.upper())
        case 7:
            print(massage.lower())
        case 8:
            print(p_(massage))
        case 9:
            print(isemail(massage))
        case 10:
            print(domen(massage))
        case 11:
            print('До новых встреч!')
            break

