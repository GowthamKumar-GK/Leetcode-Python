n=list(map(int,input().split()))
a=int(input())
r=1
for i in n:
    if i==a:
        r=0
        break
if r==0:
    print("True")
else:
    print("False")
      
       
