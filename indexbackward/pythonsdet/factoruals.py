a=10
factorial=1
if (a<0):
    print("negative")
elif (a==0):
    print("")
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print(factorial,"factorial")
    
