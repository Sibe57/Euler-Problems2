n=600851475143
m=int(n**0.5)
for i in range(m,2,-1):
    cnt=0
    for g in range(2,int((i**0.5)+1)):
        if i%g==0:
            cnt+=1
            break
    if cnt==0 and n%i==0:
        print(i)
        break
