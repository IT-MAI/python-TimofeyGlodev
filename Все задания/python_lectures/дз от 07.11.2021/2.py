n = int(input('Прошедшие минуты от начала суток- '))
a = n % (60*24)//60
b = n % 60
print(a, b)
