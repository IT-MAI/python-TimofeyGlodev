n = int(input())
F1 = 0
F2 = 1
for i in range(n):
    Fsum = F1 + F2
    F1 = F2
    F2 = Fsum
print(F1)


