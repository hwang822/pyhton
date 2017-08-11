'''
Created on Jul 14, 2016
@author: Henry Wang
   
'''

import socket
import struct
import os
import sys

#Create a ROW PACKET socket (socket.SOCK_RAW) host = 'localhost', port = 0 which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
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
#return Version, IHL, Total Length, Identification, Protocol, Source Address, Destination Address, Message for filters

def PacketsCaptureFilter(sendMessage):
#codes will be hidden
   version = ''
   IHL = ''
   totallength = ''
   ID = ''
   protocol = ''
   sourceAddr = ''
   distinationAddress = ''
   recMessage = ''

   host = socket.gethostname()
   port = 0
   server = (host, port)
   print ("Connect to server:" + str(host) + ", " + str(port))
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)	
   s.bind(server)	
   s.sendto(sendMessage.encode(), server)
   print('Conection Host Scussfully.')
   raw_data, addr = s.recvfrom(65565)
	
   unpackedData = struct.unpack('!BBHHHBBH4s4s', raw_data[:20])	    
      # print('UnpackedData: ', unpackedData)
	  
	  
	  #!{ network, B: integer 1byte, H unsigned short 2byte, s char[n]  1+1+2+2+2+1+1+2+4+4 = 20
	  # B => Version, IHL  B=> Differentiated Services, H=> Total Length
      # H => Identification   H => Flags, Fragment Offset	  
	  # B = TTL B=> Protocol, H =>Header checsum. 
 	  # 4s => Source IP address   4s => Destination IP Addresss
	  
	  
   version_IHL = unpackedData[0]
   version = version_IHL >> 4
   print('Version:\t\t', str(version))
   IHL = (version_IHL & 0xF)*4
   print('IHL:\t\t\t', str(IHL) + ' bytes')
   TOS = unpackedData[1]
   print('TOS:\t\t\t', str(hex(TOS)))
   totallength = unpackedData[2]
   print('Totallength:\t\t', str(totallength) + ' bytes')
   ID = unpackedData[3]
   print('ID:\t\t\t', str(hex(ID)) + ' (' + str(ID) + ')')
   flags  = unpackedData[4] & 0xE000   
   print('flags:\t\t\t', str(hex(flags)))   
   fragment = unpackedData[4] & 0x1FFF
   print('Fragment:\t\t', str(fragment))	  
   TTL = unpackedData[5]
   print('TTL:\t\t\t', str(TTL))
   protocol = unpackedData[6]
   print('Protocol:\t\t', str(protocol))
   checksum = unpackedData[7]
   print('Checksum:\t\t', str(checksum))
   sourceAddr = socket.inet_ntoa(unpackedData[8])
   print('Source:\t\t\t', sourceAddr)
   distinationAddress = socket.inet_ntoa(unpackedData[9])
   print('Dist:\t\t\t', distinationAddress)
   messageRc = raw_data[20:]
   print('Pay load:\t\t', messageRc)
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
   return version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc  

#Create CaptureFilterVersion(message, versionFilter) to compare default version number (4) from IPHader:   
def CaptureFilterVersion(message, versionFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(versionFilter==version):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterIHL(message, IHLFilter) to compare IHL (20) from IPHader:      
def CaptureFilterIHL(message, IHLFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(IHLFilter==IHL):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterTotallength(message, TotallengthFilter) to compare Totallength (20 + message size) from IPHader:   
def CaptureFilterTotallength(message, totallengthFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(totallengthFilter==totallength):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterID(message, TotallengthFilter) to compare ID  from IPHader:      
def CaptureFilterID(message, IDFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(IDFilter==ID):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterProtocol(message, protocolFilter) to compare Protocol # from IPHader:
def CaptureFilterProtocol(message, protocolFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(protocolFilter==protocol):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterSourceAddr(message, sourceAddrFilter) to compare SourceAddr (defaut 'localhost' ) from IPHader:
def CaptureFiltersSourceAddr(message, sourceAddrFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(sourceAddrFilter==sourceAddr):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterdistinationAddress(message, distinationAddressFilter) to compare distinationAddress (defaut 'localhost' ) from IPHader:   
def CaptureFiltersDistinationAddress(message, distinationAddressFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(distinationAddressFilter==distinationAddress):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create CaptureFilterMessage(message, messageAddressFilter) to compare message (defaut 'localhost' ) from IPHader:      
def CaptureFiltersMessage(message, messageFilter):
   filterCompare = False
   version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, messageRc = PacketsCaptureFilter(message)
   if(str(messageFilter)==str(messageRc.decode())):
       filterCompare = True
   else:
       filterCompare = False
   return filterCompare

#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    sendMessage = sys.argv[1]	
    PacketsCaptureFilter(sendMessage)
      