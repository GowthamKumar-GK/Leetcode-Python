s=['h','e','l','l','o']
stack=[]
for i in s:
    stack=stack+[i]
k=0
while len(stack)>0:
    l=stack.pop()
    s[k]=l
    k=k+1
print(s)
