def a(n):
    if n == 0:
        return 1
    return a(n-1)+n*((-1)**n)

def ad(n):
    result = 1
    for i in range(1, n+1):
        result += i*((-1)**i)
    return result

def h():
    n = 0
    result = 1
    while True:
        yield result
        n += 1
        result += n*((-1)**n)

x = h()

if __name__=="__main__":
    for i in range(0,10):
        print("a({0}) = {1:<4} {2:<4} {3:<4}".format(i, a(i), ad(i), next(x)))



