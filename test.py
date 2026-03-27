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



LISTS:



Lists allow duplicates
index based
nested lists
builtin methods like sort etc
can store different data types
ordered
dynamic---append,  


today notes:

ival[2:4] start with 2 aand exclude 4

istudent=[["venkat","8th",[1,2,3,5]],["venkasts","9th",[2,3,56,8]]]

istudent=[["venkat","8th",[1,2,3,5]],["venkasts","9th",[2,3,56,8]]]

print(istudent[1][2])



ival1=[1,2,3,4]

ival2=ival1

ival2[2]=100
print(ival1)
print(ival2)


if you change v2 it will change v1 list also

if you id(ival1) and id(ival2) it has same memory location.



if  you do ival2=ival1.copy()

also do ival2[2]=1000
then ival2 has different memory location

shallow copy:

ival1=[1,2,3,4]

ival2=ival1.copy()

ival2[2]=100
print(ival1)
print(ival2)





ival1=[1,2,[30,40]]

ival2=ival1.copy()
ival2[1]=40
ival2[2][0]=900
print(ival1)
print(ival2)




#shallow copy inner list same memory location
ival1=[1,2,[30,40]]

ival2=ival1.copy()
ival2[1]=40
ival2[2][0]=900
print(ival1)
print(ival2)





array:

electronics={"smartwatch":"500","headset":"1000"}

print(electronics)

deletevalue=electronics.pop("smartwatch")

# pop() removes by key,
print(deletevalue)

print(electronics)

merge--using unpacking


Array stores values of multiple datatype.

memory efficent,fast operations for numeric ,indexed based and mutalble nature


electronics={"smartwatch":"500","headset":"1000"}

print(electronics)

deletevalue=electronics.pop("smartwatch")

# pop() removes by key,
print(deletevalue)

print(electronics)


from array import array

avar=('i',[1,2,3,"x"])

for i in avar:
    print(i)
    

# avar1=array('i',[1,2,3,"x"])

# for i in avar1:
#     print(i)
    

avar2=array('i',[1,2,3])

for i in avar2:
    print(i)
    

avar3=array('d',[1,2,3])

for i in avar3:
    print(i)
    
    
  

avar21=array('i',[1,2,3])
avar21.insert(1,11)
avar21.append(21)
# avar21.extend(22)

print(avar21)






print(id(ival1))
print(id(ival2))

print(id(ival1[2]))
print(id(ival2[2]))



#deepcopy inner list has different location
import copy

ival3=[1,2,[50,60]]
ival4=copy.deepcopy(ival3)

ival3[1]=40
ival3[2][0]=900

print(id(ival3))
print(id(ival4))

print(id(ival3[2]))
print(id(ival4[2]))



#error exceptions
try:
    ival1= int(input("enter no1"))
    ival2= ival1+50
except Exception:
    print("some error ")
finally:
    print("execution completed")


try:
    ival1= int(input("enter no1"))
    ival2= ival1+50
except Exception:
    print("some error ")
finally:
    print("execution completed")

 
file operations:
open(filename,mode)

with open(r"C:\Users\mouni\Desktop\datas.txt", "r+") as file:
    ilog= input("enter information")
    file.write(ilog+"\n")
    file.seek(0)
   # print(file.write("\ok anna"))
   
   
with open(r"C:\Users\mouni\Desktop\datas.txt","r") as file:
     for i in file:
         print(i)

try:  
with open(r"C:\Users\mouni\Desktop\datas1.txt","r") as file:
     for i in file:
         print(i)
except Exception:
	 print("some exc")
	 
	 
try:
    with open(r"C:\Users\mouni\Desktop\datas1.txt","r") as file:
     for i in file:
         print(i)
except Exception:
	 print("some exc")

except FileNotFoundError:
    print("file not found error")
finally:
    print("file operation completed")
        

try:
    with open(r"C:\Users\mouni\Desktop\datas.txt","r") as file:
        #print(file.readline())
        for i in file:
		 print(file.readline())
         print(i)
except Exception:
	 print("some exc")

except FileNotFoundError:
    print("file not found error")
finally:
    print("file operation completed")
        

r+ → read and write, file must exist, starts at beginning
r → read only, file must exist
w → write only, creates file, deletes old content

readline() vs readlines() ,readlines creates list 

