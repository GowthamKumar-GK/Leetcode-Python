s=input()
r=''
out=''
for i in s:
    if i!=" ":
        r=r+i
    else:
        out=r+' '+out

        r=''
out=r+' '+out
        
print(out)
