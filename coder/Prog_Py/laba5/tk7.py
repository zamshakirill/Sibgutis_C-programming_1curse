email = input("Email: ")
password = input("Password: ")

def isemail(s):
    pr = [s.count("@") == 1, "." in s[s.find("@"):], not(s[0] in '.@') and not(s[-1] in '.@'), 6 <= len(s) <= 30]
    if sum(pr) == 4:
        print("Email - OK")
    else:
        print("Email - ")
        if not(pr[0]):
            print("x В вашем Email нет символа @ или его больше одного")
        if not(pr[1]):
            print("x Email должен содержать точки после @")
        if not(pr[2]):
            print("x Email не должен начинаться или заканчиваться на @ или .")
        if not(pr[3]):
            print("x Длина email должна быть от 6 до 30 символов")


def ispassword(s):
    alpha = "abcdefijklmnopqrstuvwxyz"
    numbers = "0123456789"
    spec = "!@#$%^&*"
    pr = [len(s) >= 8, any(x in numbers for x in s), any(x in alpha for x in s), any(x in alpha.upper() for x in s), any(x in spec for x in s)]
    if sum(pr) == 5:
        print("Password - OK")
    else:
        print("Password - ")
        if not(pr[0]):
            print("x Слишком короткий")
        if not(pr[1]):
            print("x Нет цифры")
        if not(pr[2]):
            print("x Нет строчной буквы")
        if not(pr[3]):
            print("x Нет заглавной буквы")
        if not(pr[4]):
            print("x Нет специального символа")


isemail(email)
ispassword(password)
