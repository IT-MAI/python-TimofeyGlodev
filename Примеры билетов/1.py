a, b, c = 10, 30, 4
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
elif b < c:
    print(b)
else:
    print(c)
# Нахождение наименьшего значения в строке

print(min(a, b, c)) # Другой вариант решения
