import math
a = int(input("Первый коэфициент:"))
b = int(input("Второй коэфициент:"))
c = int(input("Третий коэфициент:"))
D = b**2 - 4 * a * c
print(D)
if D > 0:
    print("Уравнение умеет 2 корня")
elif D == 0:
    print("Уравнение умеет 1 корень")
else:
    print("Уравнение не умеет корней")