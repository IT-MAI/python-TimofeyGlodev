def bank(a,time):
    for each_year in time:
        a = (a * 0.1)
    return a
a=float(input("Сколько денег вкладываем? "))
time=float(input("На сколько лет? "))
print(bank(a))