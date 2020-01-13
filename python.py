Microsoft Windows [Version 10.0.17134.1184]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Richa Prasad>py
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> #integer
... x=0
>>> type(x)
<class 'int'>
>>> x='Richa'
>>> type(x)
<class 'str'>
>>> x='True'
>>> type(x)
<class 'str'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> x=3.44
>>> type(x)
<class 'float'>
>>> x='Richa' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> x='Richa' + '1'
>>> x
'Richa1'
>>> type'x'
  File "<stdin>", line 1
    type'x'
          ^
SyntaxError: invalid syntax
>>> type(x)
<class 'str'>
>>> x= 3 + 2
>>> x
5
>>> x = 1.0 + 1.0j
>>> type(x)
<class 'complex'>
>>> print(x.img)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'complex' object has no attribute 'img'
>>> print(x.imag)
1.0
>>> print(x.real)
1.0
>>> x=Richa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Richa' is not defined
>>> x='Richa'
>>> print(x)
Richa
>>> 'Day' + str(1)
'Day1'
>>> str('1)
  File "<stdin>", line 1
    str('1)
          ^
SyntaxError: EOL while scanning string literal
>>> str('1')
'1'
>>> True and False
False
>>> True or False
True
>>> true and false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> true and False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> 'x' is 'x'
True
>>> 'x' is 'y'
False
>>> False
False
>>> not False
True
>>> if i<3:
...    print(i)
... i
  File "<stdin>", line 3
    i
    ^
SyntaxError: invalid syntax
>>> i=3
>>> if i<4:
...    print(i)
... i
  File "<stdin>", line 3
    i
    ^
SyntaxError: invalid syntax
>>> i=3
>>> if i<4:
...     print(i)
... i
  File "<stdin>", line 3
    i
    ^
SyntaxError: invalid syntax
>>> i=3
>>> if i<4:
...     print(i)
...
3
>>> i=3
>>> j=4
>>> k=5
>>> if i>j:
...     print(i)
... elif j>k:
...     print(j)
... else:
...     print(k)
...
5
>>>     print(k)
  File "<stdin>", line 1
    print(k)
    ^
IndentationError: unexpected indent
>>> l = list()
>>> l
[]
>>> l = ['a', 'b', 'c']
>>> l
['a', 'b', 'c']
>>> list('abcdef')
['a', 'b', 'c', 'd', 'e', 'f']
>>> l.append('c')
>>> l
['a', 'b', 'c', 'c']
>>> l.inser(0, 'a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'inser'
>>> l.insert(0, 'a')
>>> l
['a', 'a', 'b', 'c', 'c']
>>> l.append('c', 'd')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> l.append("a", "a")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> for letter in l:
...     print(letter)
...
a
a
b
c
c
>>> l = [1, 2, 3, 4, 5]
>>> for num in l:
...     print(sum(l))
...
15
15
15
15
15
>>> print(sum(l))
15
>>> l1 = ['a', 'b', 'c']
>>> print(sum(l1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> digits = [1, 5, 6]
>>> for i in digits:
...     print(i)
... else:
...     print('No items')
...
1
5
6
No items
>>> n = input("Enter no.")
Enter no.10
>>> sum = 0
>>> for num in range(0, n+1, 1):
...     sum = sum + num
... print(sum)
  File "<stdin>", line 3
    print(sum)
        ^
SyntaxError: invalid syntax
>>>
KeyboardInterrupt
>>> for num in range(0, n+1, 1):
...     sum = sum + num
...     print(sum)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> n = input("Enter no.")
Enter no.10
>>> n = int(n)
>>> sum = 0
>>> print(sum(n))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
>>> i = input("Enter no.")
Enter no.12
>>> if i%2==0
  File "<stdin>", line 1
    if i%2==0
            ^
SyntaxError: invalid syntax
>>> if (i%2 == 0)
  File "<stdin>", line 1
    if (i%2 == 0)
                ^
SyntaxError: invalid syntax
>>> if (i%2) == 0:
...     print('Even')
... else:
...     print('Odd')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting
>>>
KeyboardInterrupt
>>>