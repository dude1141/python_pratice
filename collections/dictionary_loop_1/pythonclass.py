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



