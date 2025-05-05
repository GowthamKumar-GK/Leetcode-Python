n,m=input().split()
n=int(n)
m=int(m)
text='WELCOME'
t='.|.'
for i in range(n//2+1):
    if i<(n//2):
        print((t*(2*i+1)).center(m,'-'))
    elif i==(n//2):
        print( text.center(m, '-') )
for i in range(n//2,0,-1):
    print((t*(2*i-1)).center(m,'-'))
