s=['h','e','l','l','o']
left=0
right=len(s)-1
while left<right:
    s[left],s[right]=s[right],s[left]
    right=right-1
    left=left+1
print(s)
