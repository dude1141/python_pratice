python quiz:

Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

lambda (x:x*2)
SyntaxError: invalid syntax
lambda x:x*2
<function <lambda> at 0x000001B939F0E3B0>
for i in range(3):
    print(i,end="")

    
012
for i in range(3):
    print(i)

    
0
1
2
nlist=[10,20,30]
nlist[-1]
30
nlist[1]
20
nlist[leng(nlist)-1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    nlist[leng(nlist)-1]
NameError: name 'leng' is not defined. Did you mean: 'len'?
nlist[len(nlist)-1]
30
b=(1,"2",3)
b
(1, '2', 3)
b.index(2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.index(2)
ValueError: tuple.index(x): x not in tuple
s={1,2,3,4}
print(len(s))
4




a=[1,2,3]
b=a
b.append(4)
print(a)
[1, 2, 3, 4]

x=[i **2 for i in range(5)]
print(x)
[0, 1, 4, 9, 16]



#tuples are immutable can be useed as dictoinary keys
def multiple(a,b=2):
    return a*b
result=multiply(3,4)
SyntaxError: invalid syntax
def multiple(a,b=2)
SyntaxError: expected ':'
def multiple(a,b=2):
    return a*b

multiple(3,4)
12
x=(1,2,[3,4])
x[2][0]=5
print(x)
(1, 2, [5, 4])
s1={1,2,3}
s2={3,2,6}
s1&s2
{2, 3}
nlist=[1,2,3]
for i in enumerate (nlist)
SyntaxError: expected ':'
for i in enumerate (nlist):
    print(i)

    
(0, 1)
(1, 2)
(2, 3)
#enumerate gives index
d={'a':1,'b':2}
for key,value  i in d:
    
SyntaxError: invalid syntax
for key,value, i in d:
    print(i)

    
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    for key,value, i in d:
ValueError: not enough values to unpack (expected 3, got 1)

============ RESTART: C:/Users/mouni/Downloads/pythoninstall/def1.py ===========
15

a=(1,2,3,[4,5])
a[3][1]=6
print(a)
(1, 2, 3, [4, 6])


def outer():
    x=10
    def inner():
        return x+5
    return inner

func=outer()
print(func())


def modify_list(lst):
    lst.append(4)
    lst=[1,2,3]
    return lst
l=[10,20]
result=modify_list(l)
print(l,result)

============ RESTART: C:/Users/mouni/Downloads/pythoninstall/def2.py ===========
[10, 20, 4] [1, 2, 3]


d={"a":1,"b":2}
for key,value in d.items():
    d[key]=value*2
    
print(d)
{'a': 2, 'b': 4}



myset={1,2,3}
myset.add((4,5))
print(myset)
{(4, 5), 1, 2, 3}


def test_lambda(n):
    return lambda x:x**n

square=test_lambda(2)
print(square(3))
9
print(square)
<function test_lambda.<locals>.<lambda> at 0x000001D40D529900>

Tuples are immutable
lists are mutable



a={"key1":[1,2],"key2":(3,4)}
a["key2"]+=(6,)

print(a)
{'key1': [1, 2], 'key2': (3, 4, 6)}


tup=(10,20,30)
tup.append(4)
AttributeError: 'tuple' object has no attribute 'append'

sets={1,2,3,4}
sets.add(4)
sets
{1, 2, 3, 4}




