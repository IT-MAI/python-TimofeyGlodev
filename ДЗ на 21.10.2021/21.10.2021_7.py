a = [213, -312, 36789, -1, -2, 12, 75, 78]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break