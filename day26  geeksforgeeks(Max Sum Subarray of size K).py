# Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.
# Note: A subarray is a contiguous part of any given array.
# Examples:
# Input: arr[] = [100, 200, 300, 400], k = 2
# Output: 700
# Explanation: arr2 + arr3 = 700, which is maximum.
# Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
# Output: 39
# Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
# Input: arr[] = [100, 200, 300, 400], k = 1
# Output: 400
# Explanation: arr3 = 400, which is maximum.

class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        left=0
        right=0
        maxi=0
        sum=0
        n=len(arr)
        #window acquiring
        while right <k:
            sum+=arr[right]
            right+=1
        maxi=max(maxi,sum)
        #sliding phase
        while right<n:
            sum-=arr[left]
            sum+=arr[right]
            left+=1
            right+=1
            maxi=max(maxi , sum)
        return maxi

        
