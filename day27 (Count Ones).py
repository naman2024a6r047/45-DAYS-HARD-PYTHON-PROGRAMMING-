# your code goes here
# Given a binary array of length N, find the total count of subarrays of size K with exactly M ones.
# Input Format
# The first line contains T, total number of testcases
# The first line of each testcase contains three space-separated integers N, K and M, where N represents total length of binary array, K is the size of subarray and M is the number of ones present in the subarray.
# The second line of each testcase contains N space-separated positive integers, A1, A2,A3, ......, AN.
# Output Format
# Print the total number of subarrays of size K with exactly M ones.


t= int(input())
x=0
while t>0:
    n, k, m = map(int, input().split())
    arr = list(map(int, input().split()))
    left=0
    right=0
    #lis=[]
    count_ones=0
    total_count=0
    while right<k:
        if arr[right]==1:
            count_ones+=1
        right+=1
    
    if count_ones==m:
            total_count+=1
    while right<n:
        if arr[right] == 1:
            count_ones += 1

        if arr[left] == 1:
            count_ones -= 1

        if count_ones==m:
            total_count+=1
        right+=1
        left+=1
    #print(lis)
    print(total_count)
    t-=1
