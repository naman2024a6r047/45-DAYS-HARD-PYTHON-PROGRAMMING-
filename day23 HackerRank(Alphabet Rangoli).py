def print_rangoli(size):
    # your code goes here
    tar_val =ord('a')+size-1
    for i in range(1,size+1):
        for j in range(size-i):
            print("--",end="")
        for j in range(tar_val,tar_val-i,-1):
            if i==1:
                print(chr(j),end="")
            else:
                print(chr(j),end="-")
            
        for j in range(tar_val-i+2,tar_val+1):
            if i==1:
                pass
            else:
                print(chr(j),end="")
            if j==tar_val:
                pass
            else:
                print("-",end="")
        for j in range(size-i):
            print("--",end="")
        print()
    
    ##############
    
    for i in range(1,size):
        for j in range(i):
            print("--",end="")
        for j in range(tar_val,tar_val-size+i,-1):
            if i==size-1:
                print(chr(j),end="")
            else:
                print(chr(j),end="-")
            
        for j in range(tar_val-size+i+2,tar_val+1):
           
            print(chr(j),end="")
            if j==tar_val:
                pass
            else:
                print("-",end="")
        for j in range(i):
            print("--",end="")
        print()
        
        
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
