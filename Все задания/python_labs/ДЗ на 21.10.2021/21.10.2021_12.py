a = input().split()
max = int(a[0])
max_in = 0
for i in range(1, len(a)):
    n = int(a[i])
    if n > max:
        max = n
        max_in = i
print(max, max_in)