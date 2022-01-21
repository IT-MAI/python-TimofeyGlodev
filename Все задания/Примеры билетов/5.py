a = list(range(5))
b = list(range(4))
print(a)
print(b)
c = []
for i in a:
    c.append([])
    for j in b:
        c[-1].append(i * j)
for i in c:
    print(i)
# Перемножение двух списков
