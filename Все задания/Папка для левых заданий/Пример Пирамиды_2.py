help = [""] * 100
a = ""
i = 1
n = int(input())
for i in range(1, n + 1):
    if i == 0:
        i = 1
    b = a
    a = a + str(i)

    help = sorted(list(a), reverse=True)
    for j in range(i):
        b += help[j]
    print(" " * (n - i), b)