n,m= map(int,input().split())
mid_n=n//2
x=(m//2)-1
y=1
z=(m-7)//2
for i in range(mid_n):
    for j in range(x):
        print("-",end="")
    for j in range(y):
        print(".|.",end="")
    y+=2
    for j in range(x):
        print("-",end="")
    x-=3
    print()
print("-"*z + "WELCOME" + "-"*z)
y-=2
x+=3
for i in range(mid_n):
    for j in range(x):
        print("-",end="")
    for j in range(y):
        print(".|.",end="")
    y-=2
    for j in range(x):
        print("-",end="")
    x+=3
    print()
