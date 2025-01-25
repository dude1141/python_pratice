class checkfunc:
    a=10
    b=20

    def methods3(self,n):
        if(n=="+"):
            print(self.a+self.b)
        elif(n=="-"):
            print(self.a-self.b)
        elif(n=="*"):
            print(self.a*self.b)
        else:
            print("unknown")

    def methods2(self,n1=None):
        n1=input("enter_operator:")
        self.methods3(n1)  #calling methods3 in methods2
        
        

n11=checkfunc()
n11.methods2()

        
