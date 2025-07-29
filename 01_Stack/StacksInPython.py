s = list()

msg = input("문자열 입력: ")
for c in msg:
    s.append(c)

while len(s) > 0:
    print(s.pop(), end=' ')