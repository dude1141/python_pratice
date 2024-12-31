class teset2:
    x1=100  # static variables and methods can access this
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

t1=teset2(10,20)   #object creation
#t2=teset2()
print("x...",t1.x) # calling non-static variables using object
print("y.....",t1.y)
#print("r.....",t1.r)  
t1.method1(15,25)  #calling method using obj
print("teset2",teset2.x1)
