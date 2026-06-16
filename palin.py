logic
  
 #reverse the number


#123  

# 321 if i need this i will break in to 1 2 3 seperately and then combine it reversetly, how to reverse, first break using modulus operator

#if your number is 100's multiply with 10 and 1000's then do it with 100
# and then 1000's then do it with 1000


num =123
out= num
rem=0
rev=0

if(num != 0){
    
    rem = num%10  #3 remainder 
    rev = rev*10+rem #3
    num = num/10  # 123/10 num is 12 

}
if (out==rev):
    print("palindrome")
else:
    print("not palindrome")

rem = num%10  #3 remainder 
rev = rev*10+rem #3
num = num/10  # 123/10 num is 12 


rem = num%10  #  12%10 remainder is 2
rev = rev*10+rem  3*10+2 = 32
num = num/10  #    12/10 = 1.2 is 1


rem = num%10  # 1%10 is 1
rev = rev*10+rem 32*10+1 =321
num = num/10  #  1/10 =0.1 ~0 




c=0

for i in range(1,5):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
            print('c',c)
    if (c==2):
        print("prime..>",i)


num != 0 0 !=0 stop


# Online Python - IDE, Editor, Compiler, Interpreter
num=121
rem=0 
rev=0 
k= num
while(k !=0):
    rem =k%10 
    rev =rev*10+rem
    k = k//10 
print("rev",rev)
print("num",num)
if (num == rev):
    print("palindrom", num)
else:
    print("not palindrome",num)
	
	
numbers = [1, 3, 9, 7, 15, 171, 23]

# rem =0 
rev =0 
# i= numbers 
for i in numbers:
    k=i
    rev =0 
    while (k != 0):
        rem =k%10 
        rev =rev*10+rem
        k = k//10 
    if (i == rev):
       print("palindrom", i)
    else:
      print("not palindrome",i)
    

	
	num =121

for i in range(2,num):
    if num%i ==0:
        print("not prime")
        break
else:
    print("prime")
    
    
 numbers = [1, 3, 9, 7, 15, 171, 23]
 
 since its a list you cannot see, you need to iterate each

for num in numbers:
    
    if num < 2:
        print(num, "is not prime")
        continue
    
    for i in range(2,num):
        if num%i ==0:
            print(num,"not prime")
            break
    else:
        print(num,"prime")# Online Python - IDE, Editor, Compiler, Interpreter
num=121
rem=0 
rev=0 
k= num
while(k !=0):
    rem =k%10 
    rev =rev*10+rem
    k = k//10 
print("rev",rev)
print("num",num)
if (num == rev):
    print("palindrom", num)
else:
    print("not palindrome",num)
	
	
#numbers = [1, 3, 9, 7, 15, 171, 23]

# # rem =0 
# rev =0 
# # i= numbers 
# for i in numbers:
#     k=i
#     rev =0 
#     while (k != 0):
#         rem =k%10 
#         rev =rev*10+rem
#         k = k//10 
#     if (i == rev):
#        print("palindrom", i)
#     else:
#       print("not palindrome",i)
    

	
	num =121

for i in range(2,num):
    if num%i ==0:
        print("not prime")
        break
else:
    print("prime")
    
    
 numbers = [1, 3, 9, 7, 15, 171, 23]
 
 since its a list you cannot see, you need to iterate each

for num in numbers:
    
    if num < 2:
        print(num, "is not prime")
        continue
    
    for i in range(2,num):
        if num%i ==0:
            print(num,"not prime")
            break
    else:
        print(num,"prime")
