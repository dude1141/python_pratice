a1=[100,129,999,1,2,1000]
temp=a1[0]
for i in range(0,len(a1)-1,1):
    #print(a1[i+1])
    if a1[i+1]>temp:
        temp = a1[i+1]
print(temp)

a=2
b=3
a=a+b
b=a-b
a=a-b
print(a)
print(b)


a1="MADAMS"
b=""
for i in range(-1,-7,-1):
    b=b+a1[i]
    print("b",b)
if b==a1:
    print("palindrome")
else:
    print("np")
