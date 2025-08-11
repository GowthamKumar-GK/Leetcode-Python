class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        f=sum(nums[l:r])
        c=f
        while r<len(nums):
            c=c-nums[l]+nums[r]
            if c>f:
                f=c
            l=l+1
            r=r+1
        return f/k
