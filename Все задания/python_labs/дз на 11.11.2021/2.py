def to_bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)
def func(n):
    print(int(n, base=2))
if __name__ == '__main__':
    n=input()
    func(n)