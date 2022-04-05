num=int(input())
sum=0
while num>0:

    
    
    r=num%10
    sum=sum+r
    num=num//10
    if(num==0 and sum>9):
        num=sum
        sum=0
print(sum)        
        