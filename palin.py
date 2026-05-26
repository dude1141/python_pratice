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


num != 0 0 !=0 stop


