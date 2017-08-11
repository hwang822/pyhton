'''
Created on Aug 9, 2016
@author: Henry Wang
python -m compileall NetworkAuthClientTest.py

Create TCP server to verify client user name and password

1. Create a TCP client Socket with localhost address, port number 2000, socket type as socket.SOCK_STREAM

2. The client Socket connect to the NetworkAuthServer using Localhost ddress and port number 2000.

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
import socket
import struct
import unittest

from NetworkAuthClient import NetworkAuthClientUser

#Test NetworkAuthClient with given username and password.
class TestNetworkAuthClientUser(unittest.TestCase):
    def test_NetworkAuthClientUser(self):
        NetworkAuthClientUser()
        
if __name__ == '__main__':
    unittest.main(exit=False) 
