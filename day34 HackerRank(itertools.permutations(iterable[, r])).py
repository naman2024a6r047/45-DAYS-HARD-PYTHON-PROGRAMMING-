from itertools import permutations
word,num=map(str,input().split())
sorted_word = sorted(word)
l=list(permutations(sorted_word,int(num)))
for w in l:
    print("".join(w))
