# https://www.tutorialspoint.com/python/python_cgi_programming.htm
# setup cgi at iis manager
#https://www.youtube.com/watch?v=YvN4BlLS65Y


# The Common Gateway Interface, or CGI, is a set of standards that define how information is exchanged between the web server and a custom script.

#Your browser contacts the HTTP web server and demands for the URL, i.e., filename.
#Web Server parses the URL and looks for the filename. If it finds that file then sends it back to the browser, otherwise sends an error message indicating that you requested a wrong file.
#Web browser takes response from web server and displays either the received file or error message.

#However, it is possible to set up the HTTP server so that whenever a file in a certain directory is requested that file is not sent back; instead it is executed as a program, and whatever that program outputs is sent back for your browser to display. This function is called the Common Gateway Interface or CGI and the programs are called CGI scripts. These CGI programs can be a Python Script, PERL Script, Shell Script, C or C++ program, etc.

#!/usr/bin/python

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')

#!/usr/bin/python

import os

print ("Content-type: text/html\r\n\r\n");
print ("<font size=+1>Environment</font><\br>");
for param in os.environ.keys():
   print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))