def factorial(n) :
    a = 1
    for i in range(1,n+1):
        a = i * a
    print(a)
    return a


n = int(input())
factorial(n)