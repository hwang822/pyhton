'''
Created on Jul 19, 2016
@author: Henry Wang

Trace Connection function(connectNr):

Create Socket to capture connections as packet raw at local host with connectNr.
Ouput address, time and Count in connection number evertime get package comming in until = connectNr. 
Return connected nummber

'''
import socket
import sys
from datetime import datetime


def TraceConnection(connectNr):
   connectedNo = 0
# codes will be hidden

# the public network interface
   host = socket.gethostname()
   port = 0
   server = (host, port)
# create a raw socket and bind it to the public interface
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
   s.bind(server)

# Include IP headers
   s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
   connectedNo = 0
# receive a package
   for index in range(0,connectNr):
   #while True:
      data, addr = s.recvfrom(65565)
      print (str((host, port)) + " got connection " + str(connectedNo) + " from " + str(addr) + " at " + str(datetime.now()))
      connectedNo = connectedNo+1

# disabled promiscuous mode
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
		
   return connectedNo	
 
#Create command line able to call above functions with given connectNr.	  
if __name__ == '__main__':
    connectNr = int(sys.argv[1])	
    TraceConnection(connectNr) 