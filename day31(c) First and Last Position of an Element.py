#First & Last Position of ElementGiven a sorted array of N numbers,
#find the first and last 0-based indices of a target value X in O(\log N) time. 
#Print -1 -1 if not found.
#Input: N, array elements, target X 
#Output: first_index last_index
#Example: [5, 7, 7, 8, 8, 10], X = 8 -> 3 4


# your code goes here
import bisect
n= int(input())
arr= list(map(int, input().split()))
target= int(input())
u=bisect.bisect_right(arr,target)
l=bisect.bisect_left(arr,target)
if l==n or arr[l]!= target:
    print(-1,-1)
else:
    print(l,u-1)
