n,m=map(int,input().split())
if m>n:
    lcm=n
else:
    lcm=m
while lcm:
    if(lcm%n==0 and lcm%m==0):
        print(lcm)
        break
    lcm+=1