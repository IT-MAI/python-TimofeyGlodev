a = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        a[city] = country

for i in range(int(input())):
    print(a[input()])