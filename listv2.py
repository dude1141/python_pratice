listv1=[1,2,3,4]
square=[i**2 for i in listv1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
square=[i**2 for i in listv1]
print(square)
[1, 4, 9, 16]
squares=[i**2 for i in range(1,5)]
print(squares)
[1, 4, 9, 16]
for i in list:
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    for i in list:
TypeError: 'type' object is not iterable

for i in listv1:
    print i
    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
for i in listv1:
    print(i)

    
1
2
3
4
