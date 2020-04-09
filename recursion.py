def s(n):
    if n == 0:
        return 0
    return s(n-1) + n

def s1(n):
    return n*(n+1)/2

def p(n):
    if n == 0:
        return 10000
    return p(n-1) + 0.02*p(n-1)

def p1(n):
    return (1.02**n)*10000

def b(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    return b(n-1) + b(n-2)

def c(n):
    if n == 1:
        return 9
    return 9*c(n-1) + 10**(n-1) - c(n-1)

def d(n):
    if n == 0:
        return 1
    return 3*d(n-1) + 1

def d1(n):
    return (3**(n+1) - 1)/2

# def population(year):



print(s(3))
print(s1(3))
print(p(3))
print(p1(3))
print(b(5))
print(c(5))
print(d(3))
print(d1(3))