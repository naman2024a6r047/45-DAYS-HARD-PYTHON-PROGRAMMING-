def print_formatted(number):
    # your code goes here
    x=number
    ress=""
    while x!=0:
        r=x%2
        ress+=str(r)
        x//=2
    s=len(ress)
    def deci_bin(i):
        n=i
        res=""
        while n!=0:
            r=n%2
            res+=str(r)
            n//=2
        return res[::-1]
    def deci_oct(i):
        n=i
        res=""
        while n!=0:
            r=n%8
            res+=str(r)
            n//=8
        return res[::-1]
    def deci_hex(i):
        dig={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        n=i
        res=""
        while n!=0:
            r=n%16
            if r in dig :
                res+=dig[r]
            else:
                res+=str(r)
            n//=16
        return res[::-1]
        
    for i in range(1,number+1):
        print(f"{i:>{s}} {deci_oct(i):>{s}} {deci_hex(i):>{s}} {deci_bin(i):>{s}}")
       # print(deci_oct(i),end="  ")
       # print(deci_hex(i),end="  ")
       # print(deci_bin(i),end="  ")
       # print()

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
