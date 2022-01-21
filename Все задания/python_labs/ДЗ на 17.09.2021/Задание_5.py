g = int(input())
b = g % 10
c = (g//10) % 10
d = (g//100)
print(b, c, d)
i = b * 100 + c * 10 + d
print(i)