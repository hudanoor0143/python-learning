def fib1(n):
    a =0
    b = 1
    while a<n:
        print(a, end = ' ')
        a,b = b,a+b

def fib2(n):
    a=0
    b=1
    fab = []
    while a<n:
        fab.append(a)
        a,b = b,a+b
    return fab
  