print ("Hello, Python!")

#!/usr/bin/python

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
def temp_convert(var):
   try:
      return int(var)
   except (ValueError, Argument):
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz");


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))



