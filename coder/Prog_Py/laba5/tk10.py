s = input()
sr = []
for i in range(len(s) - 1):
    if s[i + 1].isupper():
        sr.append(s[i])
        sr.append("_")
    else:
        sr.append(s[i])
sr.append(s[-1])

st = ''
for x in sr:
    st += x
print(st.lower())
