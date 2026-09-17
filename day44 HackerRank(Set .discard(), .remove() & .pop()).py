n = int(input())
s = set(map(int, input().split()))
x = int(input())

for _ in range(x):
    parts = input().split()
    task = parts[0]

    if task == "remove":
        num = int(parts[1])
        s.remove(num)
    elif task == "discard":
        num = int(parts[1])
        s.discard(num)
    elif task == "pop":
        s.remove(min(s)) 
    else:
        pass

print(sum(s))
