class reverses1:
    a1="Hello world,I am here"

    def method2(self):
        a=""
        b=reverses1.a1.split(",") #use split and then reverseit
        for i in range(len(b)-1,-1,-1):    #(b)-1 points to index 4 (start) ,-1 points to final index 0 value(hello) (Stop),-1 decrement 
            a=a+" "+b[i]
            print(a)
        print(a)


n1=reverses1()
n1.method2()
            



#this is correct if they ask only to reverse second half and donto reverse first half

input="Hello World , I Am Here"

inputlist=input.split(",")

for i in range (1,len(inputlist)):
     secondlist=inputlist[i].split(" ")
     a=""
     for i in range(len(secondlist)-1,-1,-1):
          a=a+" "+secondlist[i]
          print(a)
     print(a)
     print("atype",type(a))

str2=inputlist[0]+" ,"+str(a)
print("str2....",str2)

    
