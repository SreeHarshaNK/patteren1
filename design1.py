n = input()
n = int(n)
x = n
for i in range(1,n+1):
    print(" "*x, end="")
    for j in range(i):
        print("*",end =" ")
    print('\n')
    x = x-1
x = x+2
for i in range(n-1,0,-1):
    print(" " * x, end="")
    for j in range(i):
        print("*", end=" ")
    print('\n')
    x = x +1
