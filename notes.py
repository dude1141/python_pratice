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


#recursion 
def facto(n):
    if(n==0 or n==1):      #base case
        return 1
    else:
        return n*facto(n-1)    #recusrsion part

n=int(input("enter n value"))
res=facto(n)
print(res)



class countnumbers:
    a2=[1,2,3,5,6,7,8,9,9,9]
    
    def methodsv2(self,n):
        count=0
        for i in range(len(countnumbers.a2)):
            if n == countnumbers.a2[i]:
                count=count+1
        print(str(n)+"repated"+str(count))

n1=countnumbers()
n1.methodsv2(9)


class listsv1:
    a=["T","O","K","K","A","A"]

    def method1(self,n):
        count=0
        for  i in range(len(listsv1.a)):
            if n in listsv1.a[i]:
                count=count+1
        print(n+str(count))
        
n1=listsv1()
n1.method1("K")



class checkfunc:
    a=10
    b=20

    def methods3(self,n):
        if(n=="+"):
            print(self.a+self.b)
        elif(n=="sub"):
            print(self.a-self.b)
        elif(n=="multiply"):
            print(self.a*self.b)
        else:
            print("unknown")

n1=checkfunc()
n1.methods3("+")





