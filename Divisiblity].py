#HACK EARTH DIVISIBLITY PROGRAM
a=int(input().strip())
while True:
    s=list(map(int,input().split()))
    if len(s)!=a:
        print("Enter the correct number of items:")
    else:
        i=0
        while i!=len(s):
            n=s[i]
            out=0
            while n!=0:
                ld=n%10
                out=out*10+ld
                n=n//10
            i=i+1
        if out%10==0:
            print("Yes")
        else:
            print("No")

       #(OR)

 #to mange the time complexity
a = int(input().strip())
s = list(map(int, input().split()))

if len(s) != a:
    print("Enter the correct number of items:")
else:
    # Check if any reversed number ends with 0
    if any(str(num)[::-1][-1] == '0' for num in s):
        print("Yes")
    else:
        print("No")

