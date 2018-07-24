Basic Question
Q1. What is the difference between deep and shallow copy?

Shallow copy is used to copy the reference pointers just like it copies the values.
Deep copy is reference of  clone a new instance of original one.
l1 = l2 is shallow copy. Change l2 will effect l1

import copy
l3.copy.copy(l1).
l3 is deep copy. Change l3 will not effect l1.
Check address of object.
id(l1)=id(l2)!=id(l3). l1 and l2 is same but l3 is not.

Q2. What is the difference between list and tuples?
List are mutable it can be edited (mutable). Tuples could not be edited.

l1 = [1,2,3,4]  l1.append(10)
t1 = (1,2,3,4) t1.append(10) error.

for fixed data in or out need to tuple.
mydb = [(1,"Hello, 103), (2, "World", 204), ...]  
db contain is not fixed but item is fixed.

Q3. How Multithreading is achieved in Python?
It run threading one by one but not same time.
import multiprocessing
import threading

Q4. How can the ternary operators be used in python?

x, y = 25, 50
big = x if y < y else y

Q5. What monkey patching in Python?
In Python, the term monkey patch only refers to dynamic modifications of a class or module a runtime.
class MyClass(object):

      def f(self):

            print "f()"




def monkey_f(self):

      print "monky_f()"




x = MyClass()
x.f()
=>f()

MyClass.f = monky_f
obj = MyClass()
obj.f()
=>monkey_f()

Q6. How can you  randomize the items of a list in place in Python?
from random import shuffle
x = ['the', 'flag', 'keep', 'blue']
shuffle(x)
x = ['the', 'flag', 'keep', 'blue']

Q7. Write a sorting algorithm for a numerical dataset in Python.
list = ["1", "4", "2", "10", "5"]
list = [int(I) for I in list]
list.sort()
print (list)

Q9. Explain split(), sub(), subn() methods of "re" module in Python.
re.split(s1, s)
Q11. Explain Inheritance in Python with example?

class ParentClass(object)
    v1 = "from ParentClass - v1"
    v2 = "from ParentClass - v2"

    class ChildClass(ParentClass):
    pass

print(ChildClass.v1)
print(ChildClass.v2)

Django Question.
Q12. Mention the Diango Architecture?

Django MVT Pattern
The developer provides the Model, the view and the template then jus t maps it to a URL and Django does the magic to serve it to the user.
Django has html template view.

<html>
<head>
{{ my_title }}
</head>
<body>
{{ my_body }}
</body>
</html>

Q13. Explain how you can set up the Database in Diango?
Django uses SQLite as default database, it stores data as a single file in the file system. If you do have a database server-PostgreSQL, MySQL, Oracle, MSSQL - and want to use it rather then use your database's administration tools to create a new database for your Diango project.
setting.py
DATABASES = {
     'default': {
          'ENGINE': 'Django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
     }
}

Q14. Give an example how you can write a VIEW in Django?
from Django.http import HttpResponse
import datetime
def Current_datetime(request)
   now = datetime.datetiem.now()
   html = "<html><body>it is now %s. </body></html>"% now.
   return HttpResponse(html)
returns the current date and time, as an HTML document.

Q15. Mention what does the Django templates consists of?
The template is simple text file. It can create any text-based format like XML, CSV, HTML, etc. A template contains variables that get replaced with values when the template is evaluated and tags (% tab %) that controls the logic of the template.

DataBase <=> Model <=> View -> Templates -> Browser
                                               ^- URL <-                <- v

Q16. Explain the use of session in Django framework?

Django provides session that let you store and retrieve data on a per-site-visitor basis.

Q17. List out the inheritance styles in Django?
Abstract base classes, Multi-table inheritance, Proxy models.

Q18. Mention what does the Django field class types?
Filed Class -> The data base column type, the default HTML widget to avail while rendering a form field, The minimal validation requirements used in Django admin and in automatically generated forms.

Web Scraping Using Python Question.

Q19. Who to save an image locally using python whose URL address I already know.

import requests
url="https://www.google.com/search?tbm=isch&source=hp&biw=834&bih=510&ei=7CROW4LiFY37zgK5p4uYDQ&q=cnn&oq=cnn&gs_l=img.3..0l10.6826.7203.0.7537.7.7.0.0.0.0.114.248.2j1.3.0....0...1ac.1.64.img..4.3.247.0...0.B5Jj1SkOW3k#imgrc=YaqLHEyfeGXfTM:"
requests.get(url)

with open('image.pn', 'wb') as f:

Q20. How can I get the Google cache Age Of any URL or Web Page?

Q21. You are required to scrap data for IMDB top 250 movies page. it should only have fields moises name, year, and rating.
Data Analysis Using Python Questions.

Q22. How to get indices of N Maximum Values in A numpty Array?

Q24. What advantages does NumPy arrays offers over (nested) Python lists.

Q25. What is the difference between NumPy and SciPy?

Q26. How Do I make 3D plots/visualizations using NumPy/SciPy?

Q30 How convert a list of Dirctionaries into pandas DataFrame.

Q33. Write a program to read and write the binary data using python?

import struct
f = open(file-name, "rb")
s=f.read(9)
f.write("Hello, World!\n")
