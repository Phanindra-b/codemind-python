n=int(input())
sum=0
k=n**2
while k:
    r=k%10
    sum=sum+r
    k=k//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")