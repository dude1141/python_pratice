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
    
        
