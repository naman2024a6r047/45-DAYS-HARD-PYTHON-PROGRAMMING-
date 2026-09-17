n=int(input())
num=input().split()
s=set(map(int,num))

n1=int(input())
num1=input().split()
s1=set(map(int,num1))
s3=s.union(s1)
print(len(s3))
