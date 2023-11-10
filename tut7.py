Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> var1 = "Hello World"
>>> var2 = 256
>>> var3 = 248565.22
>>> print(var2 + var3)
248821.22
>>> var2 = Yash Rai
SyntaxError: invalid syntax
>>> var2 = "Yash Rai"]
SyntaxError: invalid syntax
>>> var2 = "Yash Rai"
>>> print(var1 + var2)
Hello WorldYash Rai
>>> var1 = "Hello World "
>>> print(var1 + var2)
Hello World Yash Rai
>>>  print(type(var1))
 
  File "<pyshell#10>", line 2
    print(type(var1))
    ^
IndentationError: unexpected indent
>>> print(type(var3))
<type 'float'>
>>> print(type(var1))
<type 'str'>
>>> print(int(var1)+ int(2))

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(int(var1)+ int(2))
ValueError: invalid literal for int() with base 10: 'Hello World '
>>> var2 = "2564"
>>> var1 = "564945"
>>> print(var1 + var2)
5649452564
>>> print(int(var1) + int(var2))
567509
>>> """ 3 types of function
str()
float()
int()
"""
' 3 types of function\nstr()\nfloat()\nint()\n'
>>> print(9* "Hello Yash")
Hello YashHello YashHello YashHello YashHello YashHello YashHello YashHello YashHello Yash
>>> print(9* "Hello Yash" )
Hello YashHello YashHello YashHello YashHello YashHello YashHello YashHello YashHello Yash
>>> print(9* "Hello Yash ")
Hello Yash Hello Yash Hello Yash Hello Yash Hello Yash Hello Yash Hello Yash Hello Yash Hello Yash 
>>> print(9* "Hello Yash \n ")
Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 Hello Yash 
 
>>> print(5* str(int(var1) + (var2)))

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(5* str(int(var1) + (var2)))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(5* str(int(var1) + (var2)))var1 = "Hello World"
SyntaxError: invalid syntax
>>> var1 = "2554"
>>> var2 = "2564"
>>> print(2 * str(int(var1) + int(var2))
      var1 = "2554"
      
SyntaxError: invalid syntax
>>> print(2 * str(int(var1) + int(var2)))
51185118
>>> print(2 * str(int(var1) + int(var2) ))
51185118
>>> print(2 * str(int(var1) +  int(var2) ))
51185118
>>> inpum = input()
print("Please Enter Your Name",)

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    inpum = input()
  File "<string>", line 1
    print("Please Enter Your Name",)
        ^
SyntaxError: invalid syntax
>>> inpum = input()
print("Please Enter Your Name")
yash rai

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    inpum = input()
  File "<string>", line 1
    yash rai
           ^
SyntaxError: unexpected EOF while parsing
>>> inpum = input()
print("Please Enter Your Name")
yash rai


Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    inpum = input()
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print("Enter Your Name")
Enter Your Name
>>> inpum = input()
456
>>> print("Enter Your Numner")
Enter Your Numner
>>> print("Enter Your Number", inpum)
('Enter Your Number', 456)
>>> inpum = input() # while writing this syntax you always remember that whatever value you entered is in string even it is int value
print("Enter Your Name")

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    inpum = input() # while writing this syntax you always remember that whatever value you entered is in string even it is int value
  File "<string>", line 1
    print("Enter Your Name")
        ^
SyntaxError: invalid syntax
>>> print("Enter Your Name")
Enter Your Name
>>> inpum = input()
456
>>> print("Enter Your Number", int(inpum) + 10)
('Enter Your Number', 466)
>>>  print("Enter First Number")
 
  File "<pyshell#50>", line 2
    print("Enter First Number")
    ^
IndentationError: unexpected indent
>>> print("Enter First Number")
Enter First Number
>>> First number = input()
SyntaxError: invalid syntax
>>> number = input()
245
>>> print("Enter second Number")
Enter second Number
>>> number2 = input()
254
>>> print("Your Number is ", int(number + number2))
('Your Number is ', 499)
>>> 
