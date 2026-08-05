from itertools import combinations

# Read input string S and integer k
S, k = input().split()

# Sort the characters of S to ensure lexicographic order
S_sorted = sorted(S)

# Generate combinations for sizes from 1 up to k
for i in range(1, int(k) + 1):
    for c in combinations(S_sorted, i):
        print("".join(c))
