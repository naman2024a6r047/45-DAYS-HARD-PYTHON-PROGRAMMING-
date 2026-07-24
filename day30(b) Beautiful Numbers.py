# Beautiful Numbers

## Problem Description
# PPA likes the digits **1, 5, and 9**. A number is considered **beautiful** if its last digit is either **1, 5, or 9**.

# Given a range $[L, R]$, your task is to determine how many beautiful numbers exist within this range (inclusive).


## Input Format
# - The first line contains a single integer $T$, representing the number of test cases.
# - Each of the next $T$ lines contains two space-separated integers $L$ and $R$.



pre=[0]*(1_00_001)
pre[1]=1
for i in range(2,1_00_001):
    val=0
    
    if i%10 in (1,5,9):
        val+=1
        
    pre[i]=pre[i-1]+val

t=int(input())

while t>0:
    l,r=map(int,input().split())
    if l==0:
        print(pre[r])
    else:
        print(pre[r]-pre[l-1])
        
    t-=1
