def zarplata(zarplata_month, percent, num_mounth):
    result = 0

    for i in range(num_mounth):
        result *= percent
        result += zarplata_month
    return result
print(zarplata(100, 1.15, 12))