#lis1=list(map(int,input().split()))
#lis2=list(map(int,input().split()))
#
#for num in lis1:
#    for num2 in lis2:
#        t=(num,num2)
#        print(t,end=" ")
        
# ideal method       
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))
