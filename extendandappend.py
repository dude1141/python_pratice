inputlst=[1,2,[14,15],7,9,18,10]
#output=[1,2,14,15,7,9,18,10]

def flatten_list(inputlst):
    l=[]
    for i in inputlst:
        print("i..",i)
        if type(i) is list:
            l.extend(flatten_list(i))
        else:
            l.append(i)
    return l

print(flatten_list(inputlst))


i    	type(i)is list?	      Action
1        	 No    	         append(1)
2        	 No             	append(2)
[14, 15]	 Yes	            extend(flatten_list([14, 15])) → [14,15]
7	         No             	append(7)
