n=int(input())
top_row = []
for i in range(2, n+1):
    row = [str(x) for x in range(1,i)]
    rev_row = sorted(row, reverse=True)
    offset = ''.join([' ' for x in range(n-i)])
    fin_row = offset + ''.join(rev_row[:len(rev_row)-1])+''.join(row)
    top_row.append(fin_row)
for x in top_row + sorted(top_row, reverse=True):
    print(x)