a=["aaaavvvvcccc","dddddaaaannn","uuuuyyyiiii"]
b=""
c=[]
for i in a:
    b=""
    for j in i:
        if j not in b:
            b=b+j
            print("b..",b)
    c.append(b)
print(c)

a="aaaavvvvcccc"
b=""
for i in a:
    if i not in b:
        b=b+i
        print("b..",b)
print(b)
        
a="HulkHulkSmash"
n=input("enter a char...")
c=0
for i in a:
    if i == n: #compare using ==
        c=c+1
print(n+str(c))
