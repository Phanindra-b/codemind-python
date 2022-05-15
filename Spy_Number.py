n=int(input())
sm=0
p=1
while n:
    r=n%10
    sm=sm+r
    p=p*r
    n=n//10
if(p==sm):
    print("Spy Number")
else:
    print("Not Spy Number")