def SubSequence(str1,str2):
    left=0#for str1
    for right in str2:
        if left<len(str1) and str1[left]==right:
            left+=1
        if left==len(str1):
            return True
    return left==len(str1)

s=input()
t=input()
print(SubSequence(s,t))
