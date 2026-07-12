def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    s="".join(l)
    # 2nd method :
    #s=string[:position]+character+string[position+1:]
    return s
    

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
