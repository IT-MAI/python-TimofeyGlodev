a = [1, 5, 4, 6, 7]
result = []
for i in range(len(a)-1):
    if a[i] < a[i+1]:
       result.append(a[i+1])
print(result)