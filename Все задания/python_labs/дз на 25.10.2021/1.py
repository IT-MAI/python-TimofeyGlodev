a = input().split()
for k in a:
    if a.count(k) > 1:
        print(k, end=' ')
        a.remove(k)