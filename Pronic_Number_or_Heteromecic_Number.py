n=int(input())
for i in range(0,n+1):
    c=i*(i+1)
    if c==n:
        print("YES")
        break
    elif i>=n//2:
        print("NO")
        break
    else:
        continue