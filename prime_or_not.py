def primeornot (a: int):
	if a<2:
		print('not prime')
		return

	for i in range(2,a):
		if a%i==0:
			print("not prime")
			return
	print ("prime...")

#above will not work
#below will work

a=3
count=0
for i in range(1,a+1):
    if a%i==0:
        count=count+1
print("count",count)
if count==2:
    print("prime")
else:
    print("not prime")
