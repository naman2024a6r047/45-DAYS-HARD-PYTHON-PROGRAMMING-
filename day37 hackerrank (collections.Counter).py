from collections import Counter

no_of_shoo = int(input())
shoo_size =list(map(int,input().split()))
data = Counter(shoo_size)
customers = int(input())
total_earned = 0
for i in range(customers):
    size , price = map(int,input().split())
    if size in shoo_size:
        if data[size]>0:
            total_earned += price
            data[size]-=1
print(total_earned)

