n=input()
p=""
k=0
for i in range(len(n)):
    if n[i]=='6'and k==0:
        p+="9"
        k+=1
    else:
        p+=n[i]
print(int(p))