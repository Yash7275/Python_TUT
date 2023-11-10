Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mystr = "Yash is good boy"
>>> print(mystr[5])
i
>>> print(mystr[0:5])
Yash 
>>> print(mystr[0:4])
Yash
>>> print(len(mystr))
16
>>> print(mystr[0:2])
Ya
>>> print(mystr[0:3])
Yas
>>> print(mystr[0:25])
Yash is good boy
>>> print(mystr[0:5:2])
Ys 
>>> print(mystr[:2])
Ya
>>> print(mystr[0:])
Yash is good boy
>>> print(mystr[::])
Yash is good boy
>>> print(mystr[::541543])
Y
>>> print(mystr[::3])
Yhso y
>>> print(mystr[-4:1:])

>>> print(mystr[-4:2:])

>>> print(mystr[-4:2])

>>> print(mystr[::-1])
yob doog si hsaY
>>> print(mystr[::-2])
ybdo iha
>>> print(mystr[::-3])
y oshY
>>> mystr = "Yash is good boy"
>>> print(mystr.isalnum())
False
>>> mystr = "Yashisgoodboy"
>>> print(mystr.isalnum())
True
>>> print(mystr.endwith("boy"))

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(mystr.endwith("boy"))
AttributeError: 'str' object has no attribute 'endwith'
>>> mystr = "Yash is good boy"print(mystr.endwith("boy"))
SyntaxError: invalid syntax
>>> 
>>> mystr = "Yash is good boy"
>>> print(mystr.endwith("boy"))

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(mystr.endwith("boy"))
AttributeError: 'str' object has no attribute 'endwith'
>>> print(mystr.endswith("boy"))
True
>>> print(mystr.endswith("bofdsy"))
False
>>> print(mystr.count])
SyntaxError: invalid syntax
>>> print(mystr.count("o")])
SyntaxError: invalid syntax
>>> print(mystr.count("o"))
3
>>> print(mystr.lower())
yash is good boy
>>> mystr = "yash is good boy"
>>> print(mystr.capital("y"))

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(mystr.capital("y"))
AttributeError: 'str' object has no attribute 'capital'
>>> print(mystr.capitalize("y"))

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(mystr.capitalize("y"))
TypeError: capitalize() takes no arguments (1 given)
>>> print(mystr.capitalize())
Yash is good boy
>>> print(mystr.upper())
YASH IS GOOD BOY
>>> print(mystr.replace("is", "are"))
yash are good boy
>>> 
