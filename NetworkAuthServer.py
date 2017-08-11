'''
Created on Aug 10, 2016
@author: Henry Wang

Create TCP server bind to localhost and portnumber 2000 to verify client user name and password

1. Create a TCP client Socket with localhost address, port number 2000, socket type as socket.SOCK_STREAM

2. The client Socket connect to the NetworkAuthServer using Localhost address and port number 2000.

3. If connect scussfully, the server will send welcome to server message and ask to entry username.

4. The client entry given user name and send to server.

5. The server verify the username. If incorrectly, the server will ask input user name again. If correctly, the server will ask input password.

6. The client entry given pass word (or reentry user name) and send to server.

7. The server verify the password with username. If incorrectly, the server will ask input password again. If correctly, the server will send message login scussfully.

8. The client could entry message to server and get echo from server.

9. The valid username and password pair:
   (user1, user11), (user2, user22), (user3, user33), (user4, user44), (user5, user55), (user6, user66), (user7, user77), (user8, user88),
   (user9, user99), (user10, user10), (user11, user1111), (user12, user1212)

'''

#!/usr/bin/python			# This is server.py file
import sys
import socket				# Import socket module
import time
from threading import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		  # Create a socket object
host = socket.gethostname() # Get local machine name
port = 2000				   # Reserve a port for your service.
s.bind((host, port))		# Bind to the port

class client(Thread):
	def __init__(self, socket, address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()
		self.userID = ''
		self.password = ''

	def run(self):
		self.sock.send(b'Welcome ' + str(self.sock).encode() + b' to Server - Please entry UserName: ')
		print('Welcome ' + str(self.sock) + ' to Server - Please entry UserName: ')
		while 1:
			data = ''
			data = self.sock.recv(1024).decode()
			if(not data):
				break								
			print('Client sent:', data)			
			if(self.userID == ''):			
				if((data == 'user1') or (data == 'user2') or (data == 'user3') or (data == 'user4') or
                  (data == 'user5') or (data == 'user6') or (data == 'user7') or (data == 'user8') or
                  (data == 'user9') or (data == 'user10') or (data == 'user11') or (data == 'user12')):
					self.sock.send(b'Please entry Password: ')
					self.userID = data
					print(b'Correct Username - Please entry Password: ')                                                            
				else: 
					self.sock.send(b'Incorrect Username - Please entry UserName: ')
					print(b'Incorrect Username - Please entry UserName: ')                                        
			elif(self.password == ''):
				if(((self.userID == 'user1') and (data=='user11')) or
				   ((self.userID == 'user2') and (data=='user22')) or
				   ((self.userID == 'user3') and (data=='user33')) or
				   ((self.userID == 'user4') and (data=='user44')) or
				   ((self.userID == 'user5') and (data=='user55')) or
				   ((self.userID == 'user6') and (data=='user66')) or
				   ((self.userID == 'user7') and (data=='user77')) or
				   ((self.userID == 'user8') and (data=='user88')) or
				   ((self.userID == 'user9') and (data=='user99')) or
				   ((self.userID == 'user10') and (data=='user1010')) or
				   ((self.userID == 'user11') and (data=='user1111')) or
				   ((self.userID == 'user12') and (data=='user1212'))):
					self.password = data
					print('login scussfully!')
					self.sock.send(b'login scussfully!')
				else:
					self.sock.send(b'Incorrect Password - Please entry Password: ')
					print(b'Incorrect Password - Please entry Password: ')                    
			else:
				self.sock.send(b'Echo: ' + data.encode())							
		
s.listen(12)					# Now wait for client connection.
print ('server at ' + str((host, port)) + ' started and listening ... ')
while 1:
	c, address = s.accept()
	client(c, address)
s.close ()