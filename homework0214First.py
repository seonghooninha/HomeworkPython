def countdown(n) :
    for i in range(0,n+1):
        print(f"{n-i}")
        if i == n:
            print("펑!!!")


n = int(input())
countdown(n)