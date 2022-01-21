def sr_znach(mass, n):
    sum = 0
    for i in range(0, n):
        sum += mass[i]
    return sum * 1.0 / n
def main():
    n = int(input())
    mass = list(map(int, input().split()))
    print(sr_znach(mass, n))
if __name__ == '__main__':
    main()


