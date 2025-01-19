class reverses1:
    a1="Hello world,I am here"

    def method2(self):
        a=""
        b=reverses1.a1.split(",") #use split and then reverseit
        for i in range(len(b)-1,-1,-1):
            a=a+" "+b[i]
            print(a)
        print(a)


n1=reverses1()
n1.method2()
            
