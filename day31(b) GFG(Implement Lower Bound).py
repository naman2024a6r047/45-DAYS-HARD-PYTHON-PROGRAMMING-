class Solution:
    def lowerBound(self, arr, target):
        left=0
        right=len(arr)-1
        res=-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>=target:
                res=mid
                right=mid-1
            else:
                left=mid+1
        if res==-1:
            return len(arr)
        return res
