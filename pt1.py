def pi(n):
    total = 3
    for i in range(n-1):
        if (i+1)%2 != 0:
            x = (i+1)*2
            y = 4/(x*(x+1)*(x+2))
            total+=y
        elif (i+1)%2 == 0:
            a = (i+1)*2
            b = 4/(a*(a+1)*(a+2))
            total-=b
    print(f"pi({n})={total}")

pi(1)
pi(2)
pi(3)