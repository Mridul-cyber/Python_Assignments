#1. Write a python script to add comments and print “Learning Python” on screen

#This is Single line comment.


print("\"Learning Python\"")

#2. Write a python script to add multi line comments and print values of four variables, each in a new line. Variable contains any values.

"""This is 
multi-
-line
Comment"""

""" a = 4.5    
b = "Mridul"
c = 23
d = True

print(a,b,c,d,sep="\n") """



#3. Write a python script to print types of variables. Create 5 variables each of them containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)

a = 35
b = "MySirG"
c = 5.46
d = 3+4j


print(type(a))
print(type(b))
print(type(c))
print(type(d))

#4. Write a python script to print the id of two variables containing the same integer values

a = 56
b = 56

print(id(a))
print(id(b))


#5 . Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable

a = 23
b = "mridul"
c = 66.2
d = True

print(type(a),id(a))
print(type(b),id(b))
print(type(c),id(c))
print(type(d),id(d))

print()

#6.  Write a python script to print all the keywords

""" import keyword
print(keyword.kwlist) """

""" from keyword import kwlist
print(kwlist) """

print("this is keywords list  ")
print()
from dataclasses import dataclass
from email.utils import localtime
from keyword import *
from time import ctime, strftime
print(kwlist)



#7. On Python shell use help() function and display the list of keywords

#help("keywords")

""" #8. Create two Python files A0.py and A1.py. Create a variable in A1.py and assign some
value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py  """

#Done 


#9 .  Name the keywords, used as data in the Python script.

a = True
b = False
c = None

d = a * 5  #True = 1 
print(d)

e = b + 5  #False = 0 
print(e)

""" f = c  + 2
print(f)   #TypeError  """


"""Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)"""


from datetime import * 

today_date = date.today()
today_time = strftime("%H - %M - %S")
print("Date: " , today_date)
print("Time: " , today_time)
