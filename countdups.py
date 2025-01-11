class reversess:
    a1="DRAMAAAATIC"

    def method2(self):
        a=0
        for i in range(len(reversess.a1)):
            if i>=1:
                if reversess.a1[i]==reversess.a1[i-1]:
                    a=a+1
        if (a>=1):
            print("string has dupicates")
        else:
            print("has no dup")


n1=reversess()
n1.method2()
