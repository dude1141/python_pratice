class names:
    def method2(self,name):
        if (name=="morning"):
            print("hello good morning")
        elif(name=="afternoon"):
                print("hello good evening")
        else:
            print("good night")
	  
n2=names()
name1=input("enter string")
n2.method2(name1)



class evenorodd:
    alist=(1,2,4,55,666,89)
    
    def evenoroddmethod1(self):
        for i in range(len(evenorodd.alist)):
            if i%2==0:
                print("even",evenorodd.alist[i])
            else:
                print("odd",evenorodd.alist[i])
    
n1=evenorodd()
n1.evenoroddmethod1()
