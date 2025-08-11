def Container(n):
    l=0
    r=len(n)-1
    res=0
    while l<r:
        d=r-l
        m=min(n[l],n[r])
        f=d*m
        if f>res:
            res=f
        elif n[l]>n[r]:
            r-=1
        else:
            l=l+1
    return res
n=list(map(int,input().split()))
print(Container(n))
