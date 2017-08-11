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
   server = (host, port) # need same port at server
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
   print('Version:\t\t', str(version) + " - " + getVersionDesc(version))
   IHL = (version_IHL & 0xF)*4
   print('IHL:\t\t\t', str(IHL) + ' bytes')
   TOS = unpackedData[1]
   prcencedence, delay, throughput, reliability, cost = getTOS(TOS)
   print('TOS:\t\t\t', str(hex(TOS)) + " - " + prcencedence + ", " + delay + ", " + throughput + ", " + reliability + ", " + cost)
   totallength = unpackedData[2]
   print('Totallength:\t\t', str(totallength) + ' bytes')
   ID = unpackedData[3]
   print('ID:\t\t\t', str(hex(ID)) + ' (' + str(ID) + ')')
   flags  = unpackedData[4] & 0xE000
   flagR, flagD, flagM = getFlags(flags)
   print('flags:\t\t\t', str(hex(flags)) + " - " + flagR + ", " + flagD + ", " + flagM)   
   fragment = unpackedData[4] & 0x1FFF
   print('Fragment:\t\t', str(fragment))	  
   TTL = unpackedData[5]
   print('TTL:\t\t\t', str(TTL))
   protocol = unpackedData[6]
   print('Protocol:\t\t', getProtocol(protocol))
   checksum = unpackedData[7]
   print('Checksum:\t\t', str(checksum))
   sourceAddr = socket.inet_ntoa(unpackedData[8])
   print('Source:\t\t\t', sourceAddr)
   distinationAddress = socket.inet_ntoa(unpackedData[9])
   print('Dist:\t\t\t', distinationAddress)
   recMessage = raw_data[20:]
   print('Pay load:\t\t', recMessage)
   s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
   
   return version, IHL, totallength, ID, protocol, sourceAddr, distinationAddress, recMessage  

#Create get ip text information functions based on the header information.
#getProtocol()(IPheader):, getVersionDesc()(IPheader):, getTOS(IPheader):   

# Version#: Description 
# 0: reserved. 4: IP, Internet Protocol. 5: ST, ST Datagram Mode. 6: SIP, Simple Internet Protocol. SIPP, Simple Internet Protocol Plus. IPv6, Internet Protocol.
# 7: TP/IX, The Next Internet. 8: PIP, The P Internet Protocol. 9: TUBA. 15: reserved.
def getVersionDesc(version):
#codes will be hidden
   versionDesc = ''
   
   if(version==0):
      versionDesc = "reserved." 
   elif(version==4):
      versionDesc = "IP, Internet Protocol."  
   elif(version==5):
      versionDesc = "ST, ST Datagram Mode."
   elif(version==6):
      versionDesc = "SIP, Simple Internet Protocol. SIPP, Simple Internet Protocol Plus. IPv6, Internet Protocol."
   elif(version==7):
      versionDesc = "TP/IX, The Next Internet."
   elif(version==8):
      versionDesc = "PIP, The P Internet Protocol."
   elif(version==9):
      versionDesc = "TUBA."
   elif(version==15):
      versionDesc = "reserved."
   else: 
      versionDesc = ""
   
   return versionDesc
   
# TOS 	  
# 00 01 02   03 04 05 06 07 (bit)
# Precedence D T R M 0 
# Precedence. 3 bits. [Value: Description]
# [0: Routine, 1: Priority, 2: Immediate, 3: Flash, 4: Flash override, 5: CRITIC/ECP, 6: Internetwork control, 7: Network control]. 
# D (Minimize delay). 1 bit. T (Maximize throughput). 1 bit.  R (Maximize reliability). 1 bit. M (Minimize monetary cost). 1 bit.
# [0: Normal delay, 1: Low delay] [0: Normal throughput. 1: High throughput] [0: Normal reliability, 1: High reliability] [0: Normal monetary cost, 1: Minimize monetary cost] 	  
def getTOS(IPHader):
   #codes will be hidden

   prcencedence = ''   
   delay = ''
   throughput = ''
   reliability = ''
   cost = ''   
   
   prcencedence = {0: "Routine", 1: "Priority", 2: "Immediate", 3: "Flash", 4: "Flash override", 5: "CRITIC/ECP", 6: "Internetwork control", 7: "Network control"}   
   delay = {0: "Normal delay", 1: "Low delay"}
   throughput = {0: "Normal throughput", 1: "High throughput"}
   reliability = {0: "Normal reliability", 1: "High reliability"}
   cost = {0: "Normal monetary cost", 1: "Minimize monetary cost"}   
   D = IPHader & 0x10
   D >> 4
   T = IPHader & 0x8
   T >> 3
   R = IPHader & 0x4
   R >> 2
   M = IPHader & 0x2
   M >> 1 
   return prcencedence[IPHader >> 5], delay[D], throughput[T], reliability[R], cost[M]

# Flags. 3 bits. [Value: Description]
# [00: R, 01: DF, 02: MF].    
def getFlags(data):
   flagR = ''
   flagDF = ''
   flagMF = ''
#codes will be hidden
   flagR = {0: "Reserved"}
   flagDF = {0: "Fragment if necessary", 1: "Do not fragment"}
   flagMF = {0: "This is the last fragment", 1: "More fragments follow this fragment"}   
   R = data & 0x8000
   R >> 15
   D = data & 0x4000
   D >> 14
   M = data & 0x2000
   M >> 13
   return flagR[R], flagDF[D], flagMF[M]
   
#read and parse protocol information from protocol.txt 
def getProtocol(protocolNr):
#codes will be hidden
   protocolDesc = ''
   protocolFile = open('protocol.txt', 'r')
   for line in protocolFile:
      a, b = line.split(' ', 1)
      if(int(a) == protocolNr):
         protocolDesc = b.rstrip(os.linesep)
         return protocolDesc 
   return 'Involid protocol number'
   
#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
#code will be hidden
    sendMessage = sys.argv[1]	
    PacketsAnalysis(sendMessage)
	
