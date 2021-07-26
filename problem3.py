# Листинг 7
y=600851475143
n=int(y**0.5)
lst=[2]
for i in range(3, n+1, 2):
	if (i > 10) and (i%10==5):
		continue
	for j in lst:
		if j*j-1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)
y=600851475143
counter=-1
while True:
    if y%lst[counter]==0:
        print(lst[counter])
        print(counter)
        break
    else:
        counter-=1
print("end")