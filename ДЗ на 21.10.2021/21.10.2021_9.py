a = [int(i) for i in input().split()]
c = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        c += 1
print(c)