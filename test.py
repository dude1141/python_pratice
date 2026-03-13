a="clound computing tel"
print(a[-16:])

print(a.replace("tel","sss",2))


email="admin@gmail.com"
print(email.find("@")+1)
print(email[email.find("@")+1:])
print(email[6:])





function and lambda:

def numberadd(ival1,ival2):
    ival1+ival2
    return ival1+ival2


rest=numberadd(5,6)
print(rest)



def numberadd(ival1,ival2):
    ival1+ival2
    return ival1+ival2


ival1= int(input("Enter first value:"))
ival2= int(input("Enter second value:"))
rest=numberadd(ival1,ival2)
print(rest)


def numberadd(*vals):
    #return ival1+ival2
     return sum(vals)

rest=0
rest=numberadd(5,7,8)
print(rest)


rest=lambda x,y: x*y
print("multplication of two numbers",rest(9,10))


