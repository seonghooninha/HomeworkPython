def countdown(n):
    if n == 0:
        print(n)
        print("펑!!!")
        return
    print(n)
    countdown(n-1)

n = int(input())
countdown(n)