class Solution:
    def upperBound(self, arr, target):
        l=0
        h=len(arr)-1
        ans=-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>target:
                ans=mid
                h=mid-1
            else:
                l=mid+1
                
        if ans==-1:
            return len(arr)
        else:
            return ans
