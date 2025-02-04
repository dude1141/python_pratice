a=int(input("emter a"))
b=int(input("enter b"))
try:
    if b==0:
        raise Exception("Exception raised")
    print("C",a/b)
except Exception as e:
    print(e)
        
