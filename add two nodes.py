l1= list(map(int,input().split()))
l2= list(map(int,input().split()))
s=0
s1=0
for i in l1:
    if type(i)==int:
        while i!=0:
            ld=i%10
            s=s*10+ld
            #print(s)
            i=i//10
for i in l2:
    if type(i)==int:
        while i!=0:
            ld=i%10
            s1=s1*10+ld
            #print(s1)
            i=i//10
res=s+s1
r=[]
while res!=0:
    ld=res%10
    r=[ld]+r
    res=res//10
print(r)


