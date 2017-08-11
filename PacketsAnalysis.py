'''
Created on Jul 14, 2016
@author: Henry Wang

'''
import socket
import struct
import os
import sys

#Create a ROW PACKET socket (host = 'localhost', port = 0, socket type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
#Receive a packet from the created socket of local host with IPheader + Message + Address.
#Unpacket IPHeader as below table.
'''
IPHader format:

    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |Version|  IHL  |Type of Service|          Total Length         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |         Identification        |Flags|      Fragment Offset    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |  Time to Live |    Protocol   |         Header Checksum       |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                       Source Address                          |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Destination Address                        |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                    Options                    |    Padding    |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   
'''
#return Version, IHL, Total Length, Identification, Protocol, Source Address, Destination Address, Message
def PacketsAnalysis(sendMessage):
   version = ''
   IHL = ''
   totallength = ''
   ID = ''
   protocol = ''
   sourceAddr = ''
   distinationAddress = ''
   recMessage = ''
   
   return version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, recMessage  

#Create get ip text information functions based on the header information.
#getProtocol()(IPheader):, getVersionDesc()(IPheader):, getTOS(IPheader):   

# Version#: Description 
# 0: reserved. 4: IP, Internet Protocol. 5: ST, ST Datagram Mode. 6: SIP, Simple Internet Protocol. SIPP, Simple Internet Protocol Plus. IPv6, Internet Protocol.
# 7: TP/IX, The Next Internet. 8: PIP, The P Internet Protocol. 9: TUBA. 15: reserved.
def getVersionDesc(version):
   versionDesc = ''
      
   return versionDesc
   
# TOS 	  
# 00 01 02   03 04 05 06 07 (bit)
# Precedence D T R M 0 
# Precedence. 3 bits. [Value: Description]
# [0: Routine, 1: Priority, 2: Immediate, 3: Flash, 4: Flash override, 5: CRITIC/ECP, 6: Internetwork control, 7: Network control]. 
# D (Minimize delay). 1 bit. T (Maximize throughput). 1 bit.  R (Maximize reliability). 1 bit. M (Minimize monetary cost). 1 bit.
# [0: Normal delay, 1: Low delay] [0: Normal throughput. 1: High throughput] [0: Normal reliability, 1: High reliability] [0: Normal monetary cost, 1: Minimize monetary cost] 	  
def getTOS(IPHader):

   prcencedence = ''   
   delay = ''
   throughput = ''
   reliability = ''
   cost = ''   
   
   return prcencedence[IPHader >> 5], delay[D], throughput[T], reliability[R], cost[M]

# Flags. 3 bits. [Value: Description]
# [00: R, 01: DF, 02: MF].    
def getFlags(data):
   flagR = ''
   flagDF = ''
   flagMF = ''

   return flagR[R], flagDF[D], flagMF[M]
   
#read and parse protocol information from protocol.txt 
def getProtocol(protocolNr):
   protocolDesc = ''

   return 'Involid protocol number'
   
#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    sendMessage = sys.argv[1]	
    PacketsAnalysis(sendMessage)
	
