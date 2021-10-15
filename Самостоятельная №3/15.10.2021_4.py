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

#оба верные

n = int(input())
for i in range(2, n+1):

    row = [str(x) for x in range(1,i)]

    rev_row = sorted(row, reverse=True)

    offset = ''.join([' ' for x in range(n-i)])

    fin_row = offset + ''.join(rev_row[:len(rev_row)-1])+''.join(row)

    print(fin_row)