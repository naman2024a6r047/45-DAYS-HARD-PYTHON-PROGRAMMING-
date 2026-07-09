if __name__ == '__main__':
    N = int(input())
    lis=[]
    for i in range(N):
        inst = input().split()
        if inst[0]=="insert":
            lis.insert(int(inst[1]),int(inst[2]))
        if inst[0]=="print":
            print(lis)
        if inst[0]=="remove":
            lis.remove(int(inst[1]))
        if inst[0]=="append":
            lis.append(int(inst[1]))
        if inst[0]=="sort":
            lis.sort()
        if inst[0]=="pop":
            lis.pop()
        if inst[0]=="reverse":
            lis.reverse()

    
        
