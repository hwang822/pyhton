# https://www.tutorialspoint.com/python/python_cgi_programming.htm
# setup cgi at iis manager
#https://www.youtube.com/watch?v=YvN4BlLS65Y


# The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between the web server and a custom script.

#Your browser contacts the HTTP web server and demands for the URL, i.e., filename.
#Web Server parses the URL and looks for the filename. If it finds that file then sends it back to the browser, otherwise sends an error message indicating that you requested a wrong file.
#Web browser takes response from web server and displays either the received file or error message.

#However, it is possible to set up the HTTP server so that whenever a file in a certain directory is requested that file is not sent back; instead it is executed as a program, and whatever that program outputs is sent back for your browser to display. This function is called the Common Gateway Interface or CGI and the programs are called CGI scripts. These CGI programs can be a Python Script, PERL Script, Shell Script, C or C++ program, etc.

#!/usr/bin/python

#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

# Get data from fields
if form.getvalue('maths'):
   math_flag = "ON"
else:
   math_flag = "OFF"

if form.getvalue('physics'):
   physics_flag = "ON"
else:
   physics_flag = "OFF"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
print ("</body>")
print ("<body>")
print ("<h2> CheckBox Maths is : %s</h2>" % math_flag)
print ("<h2> CheckBox Physics is : %s</h2>" % physics_flag)
print ("</body>")
print ("</html>")