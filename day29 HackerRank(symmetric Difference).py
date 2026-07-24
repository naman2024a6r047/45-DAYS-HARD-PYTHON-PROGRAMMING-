m= int(input())
s1=set()
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))

U=s1.union(s2)
A=s1.intersection(s2)
symetric_diff=U.difference(A)
for num in sorted(symetric_diff):
    print(num)
