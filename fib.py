spisok = [0,1]
t = 0
while True:
    n = spisok[t] + spisok[t+1]
    spisok.append(n)
    t = t+1
    if t == 50:
        print(spisok)
        break
