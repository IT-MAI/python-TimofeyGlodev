n=int(input())
S= []
for i in range(n):
    row = [1]*(i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = S[i-1][j-1]+S[i-1][j]
    S.append(row)
for r in S:
    print(r)