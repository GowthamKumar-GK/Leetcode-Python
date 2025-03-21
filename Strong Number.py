n=int(input())
r=n
s=0
while n!=0:
    ld=n%10
    i=1
    product=1
    while i<=ld:
        product=product*i
        i=i+1
    s=s+product
    #print(s)
    n=n//10
if s==r:
    print("Strong Number")
else:
    print("Not a strong number")
    
