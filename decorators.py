def smartdiv(func):
    def innerfunc(x,y):
        if y==0:
            print("cannot divide")
        else:
            print("divided by outpout",x/y)

        return func(x,y)
    return innerfunc


@smartdiv  #calling decoration function
def godivide(a,b):
    return a/b

print(godivide(20,2))

