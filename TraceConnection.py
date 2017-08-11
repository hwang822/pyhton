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
		
   return connectedNo	
 
#Create command line able to call above functions with given connectNr.	  
if __name__ == '__main__':
    connectNr = int(sys.argv[1])	
    TraceConnection(connectNr) 