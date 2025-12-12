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


i.. 1
append []
i.. 2
append [1]
i.. [14, 15]
i.. 14
append []
i.. 15
append [14]
i.. 7
append [1, 2, 14, 15]
i.. 9
append [1, 2, 14, 15, 7]
i.. 18
append [1, 2, 14, 15, 7, 9]
i.. 10
append [1, 2, 14, 15, 7, 9, 18]
[1, 2, 14, 15, 7, 9, 18, 10]


append just appends,length increases by 1
extends add each element as iterable
