class test3:
    alist=[1,2,3,4]  #static variable should be accessed with class-name and non-static using self.name
    a=0
    
    def method1(self):    
        for i in range(len(test3.alist)):
            print(test3.alist[i])
            if (i ==2):
                break

n1=test3()
n1.method1()
