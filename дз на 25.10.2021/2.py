a = int(input())
if a == 0:
    print(0)
else:
    f_1 = 0
    f_2 = 1
    n = 1
    while f_2 <= a:
        if f_2 == a:
            print(n)
            break
        f_1, f_2 = f_2, f_1 + f_2
        n += 1
    else:
        print(-1)