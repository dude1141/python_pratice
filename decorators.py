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






def upper_case1(function):
        def wrapper():
                func=function()
                a=func.upper()
                return a  #function should retrun something
        
        return wrapper

def say_hi():
    return 'hello there'

decorate = upper_case1(say_hi)
print(decorate())

#decorate() runs wrapper().
#wrapper() calls say_hi(), which returns 'hello there'.
#'hello there' is converted to 'HELLO THERE'.
#'HELLO THERE' is returned and printed.
