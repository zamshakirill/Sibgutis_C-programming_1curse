text = input()
word = input()
k = 0
for i in range(len(word)):
    if word[i] in text:
        k += 1
        text = text[text.find(word[i]):]
if k == len(word):
    print('True')
else:
    print('False')

