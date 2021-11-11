def gcd(n, m): #Функция
    result = 1
    for i in range(1,n + 1):
        if n % i == 0 and m % i == 0:
            result = i
    return n * m // result
print(gcd(9, 6)) #Нахождение наименьшего общего кратного
