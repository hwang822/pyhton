# tps://www.tutorialspoint.com/python/index.htm

# ython is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable.


print ("Hello, Python!")

#!/usr/bin/python

# Python - Variable Type 
print ("\nPython - Variable Type\n")

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print (counter)
print (miles)
print (name)

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# Python - Basic Operators 
print ("\nPython - Basic Operators\n")

# Arithmetic Operators
# Comparison (Relational) Operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators


# Python - Decision Making 
print ("\nPython - Decision Making\n")

var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")

# Loops 
print ("\nLoops\n")

# while, for, do.

# Python - Numbers 
print ("\nPython - Numbers\n")

# Python - Strings 
print ("\nPython - Strings\n")

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
print (u'Hello, world!')

# Python - Lists
print ("\nPython - Lists\n")

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001;
print ("New value available at index 2 : ")
print (list[2])

list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)
del (list1[2]);
print ("After deleting value at index 2 : ")
print (list1)

# Python - Tuples
print ("\nPython - Tuples\n")

# A tuple is a sequence of immutable Python objects. 
# Tuples are sequences, just like lists. The differences between tuples and lists are, 
# the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.
#
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);

# Python - Dictionary
print ("\nPython - Dictionary\n")

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

# Python - Date & Time
print ("\Python - nDate & Time\n")

import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

import calendar

cal = calendar.month(2018, 3)
print ("Here is the calendar:")
print (cal)

# Python - Functions
print ("\nPython - Functions\n")

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

     
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)   

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total)

# Python - Modules

print ("\nPython - Modules\n")
# a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

#Python code for a module named aname normally resides in a file named aname.py

# Import module support
import aname

# Now you can call defined function that module as follows
aname.print_func("Zara")

# Python - Files I/O
print ("\nPython - Files I/O\n")

# Open a file
fo = open("employees.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()

# Python - Exceptions Handling
print ("\nPython - Exceptions Handling\n")

# Define a function here.
#def temp_convert(var):
#   try:
#      return int(var)
#   except (ValueError, Argument):
#      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
#temp_convert("xyz");


#def KelvinToFahrenheit(Temperature):
#   assert (Temperature >= 0),"Colder than absolute zero!"
#   return ((Temperature-273)*1.8)+32
#print (KelvinToFahrenheit(273))
#print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))



