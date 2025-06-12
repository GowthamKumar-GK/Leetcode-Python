l=list(map(int,input().split()))
out=0
i=0
s=[]
while i<len(l):
    out=out*10+int(l[i])
    i=i+1
out=out+1
#s=list(map(int, str(out)))
while out>0:
    ld=out%10
    s.append(ld)
    out=out//10
s.reverse()
print(s)


'''class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        out = 0
        i = 0
        s = []
        while i < len(digits):
            out = out * 10 + int(digits[i])
            i = i + 1
        out = out + 1
        while out > 0:
            ld = out % 10
            s.append(ld)
            out = out // 10
        s.reverse()
        return s
        '''
