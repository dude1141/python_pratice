#remove value in list

list1=[10,11,12,34,45,17]
unwanted_list=[10,11,12]

list2=[a for a in list1 if a not in unwanted_list]
print(list2)
[34, 45, 17]


or
list1.pop(1)

#find string in list
list=["DDDDDD",1,2,3,"bocchu"]
s="bocchu"
d=[i for i in list if s in list]
if len(d)>0:
    print(s)

