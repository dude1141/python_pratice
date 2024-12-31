#constructor overloading
class test3:
    x1=100  #static variables and methods can access this
    def __init__(self,a,b):   #constructor with parameters
        self.x=a   #non static variables x and y
        self.y=b   # a and b are local variables
        print("self.x",self.x)
        print("self.y",self.y)
        
    def __init__(self,a,b,c):   #constructor with parameters
        self.x=a   #non static variables x and y
        self.y=b   # a and b are local variables
        self.z=c
        print("self.x",self.x)
        print("self.y",self.y)
        print("self.z",self.z)
        
    def method1(self,p,q):    
        r=p+q                 #p,q ,r,s are local variables
        s=self.x+self.y       # sum of non-static variables
        print("r=...inside method",r)
        print("s=...inside method.",s)


t1=test3(10,20)
#try with three params
