Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p=float(input("enter principal:"))
enter principal:10
>>> r=float(input("enter rate:"))
enter rate:22
>>> t=float(input("enter time:"))
enter time:4
>>> si=(p*r*t)/100
>>> print("simple interest=",si)
simple interest= 8.8
>>> a=int(input("enter first number:"))
enter first number:10
>>> b=int(input("enter second number:"))
enter second number:22
>>> ifa>b:
	
SyntaxError: invalid syntax
>>> if a>b:
	print("maximum=",a)
	else:
		
SyntaxError: invalid syntax
>>> print("maximum=",b)
maximum= 22
>>> for i in range(1,6):
	print(i)

	
1
2
3
4
5
>>> s= input("enter string:")
enter string:22
>>> print("length=",len(s))
length= 2
>>> print("welcome to python programming!")
welcome to python programming!
>>> s= input("enter string:")
enter string:10
>>> print("first character=",s[0])
first character= 1
>>> s= input("enter character=",s[-1])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s= input("enter character=",s[-1])
TypeError: input expected at most 1 arguments, got 2
>>> 
>>> s= input("enter string:")
enter string:10
>>> print("last character=",s[-1])
last character= 0
>>> n= int(input("enter number:"))
enter number:22
>>> if n>0:
	print("positive number")

	
positive number
>>> elif n<0:
	
SyntaxError: invalid syntax
>>> print("negative number")
negative number
>>> else:
	
SyntaxError: invalid syntax
>>> print("zero")
zero
>>> a= int(input("enter first number:"))
enter first number:10
>>> b= int(input("enter second number:"))
enter second number:22
>>> c= int(input("enter third number:"))
enter third number:04
>>> sum = a+b+c
>>> print("sum=",sum)
sum= 36
>>> x = input("enter anything:")
enter anything:10
>>> print("you entered:",x)
you entered: 10
>>> 