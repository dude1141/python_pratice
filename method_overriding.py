class test2:
    x1=100  #static variables and methods can access this
    def __init__(self,a,b):   #constructor with parameters
        self.x=a   #non static variables x and y
        self.y=b   # a and b are local variables
    def method1(self,p,q):    
        r=p+q                 #p,q ,r,s are local variables
        self.x=p              # non-static variables override
        self.y=q
        s=self.x+self.y       # sum of non-static variables
        print("r=...inside method",r)
        print("s=...inside method.",s)
class test3(test2):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.z=c
    def method1(self,p,q):
        super().method1(p,q)
        t=p*q
        self.z=t
        print("t...inside childtest",t)
        print("t...inside childtest",self.z)

t2=test3(10,20,30)
t2.method1(100,200)
        
        
