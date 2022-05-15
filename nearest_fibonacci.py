n=int(input())
a,b=0,1
c=a+b
while c<=n:
    a=b
    b=c
    c=a+b
d2=abs(n-c)
d1=abs(n-b)
if d1>d2:
    print(c)
elif d1<d2:
    print(b)
elif d1==d2:
    print(b,c)