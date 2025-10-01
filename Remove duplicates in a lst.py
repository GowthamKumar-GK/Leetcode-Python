"""nums=[0,0,1,1,1,2,2,3,3,4]
c=0
s=[]
for i in nums:
    if i not in s:
        s=[i]+s
        c=c+1

print(c)"""
class Solution:
    def removed(self,lst):
        c=0
        s=[]
        for i in lst:
            if i not in s:
                s=s+[i]
                c=c+1
        return c,s
        

if __name__ == "__main__":
    s =[1,1,2]
    solution = Solution()
    print(solution.removed(s))  # Output: True
