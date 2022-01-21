m1 = [[2, 3], [4. 5]]
m2 = [[8, 1], [9, 6]]
m3 = []
for i in range(2):
    m3.append([])
    for j in range(2):
        x = m1[i][j] + m2[i][j]
        m3[i].append(x)