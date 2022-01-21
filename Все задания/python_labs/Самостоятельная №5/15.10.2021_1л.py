a = [1, 2, 6, 7, 65]
result = []
for x in range(len(a)):
    if a[x] % 2:
        result.append(a[x])
print(result)
