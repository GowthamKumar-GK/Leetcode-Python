n=int(input())
s=str(n)
out=0
if len(s)<2:
    print("invalid atleast three digit number")
else:
    for i in range (len(s)):
        if i!=(len(s)-1):
            out=out+int(s[i])
    print(out)
    if out==int(s[-1:]):
        print("done")
    else:
        print("sorry")
    


        
