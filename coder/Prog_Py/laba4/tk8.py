letter1 = input()
num1 = int(input())
letter2 = input()
num2 = int(input())
if abs(ord(letter1) - ord(letter2)) == abs(num1 - num2):
    print('YES')
else:
    print('NO')
    