from itertools import combinations_with_replacement
words , num =input().split()
sorted_words =sorted(words)
for word in (combinations_with_replacement(sorted_words,int(num))):
    print("".join(word))
