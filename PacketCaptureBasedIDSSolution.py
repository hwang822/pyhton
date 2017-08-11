'''
Created on Aug 9, 2016
@author: Henry Wang

Creating a intrusion detection system. Sniff all of the IP packets using a raw socket.
Raw socket is a socket the sends and receives data in binary.
IDS read an IP packet and analyze the received packet in binary according to the IP protocol.

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

import socket
import struct

#Create RAW socket and bind to (localhost, 0). recvfrom packet (header + playload), 
#parse IPheader then reutrn packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload for test analyze   

def PacketCaptureBasedIDSAnalyze():
    packet = None
    receiveraddress = ''
    version = ''
    IHL = ''
    totallength = ''
    ID = ''
    protocol = ''
    sourceAddress = ''
    distinationAddress = ''
    playload = ''


    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
    s.bind((socket.gethostname(),0))
    s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
    s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

    packet, receiveraddress = s.recvfrom(10000)
    print(packet)
    unpackedData = struct.unpack('!BBHHHBBH4s4s', packet[:20])	    
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
    print('Protocol:\t\t', protocol)
    checksum = unpackedData[7]
    print('Checksum:\t\t', str(checksum))
    sourceAddress = socket.inet_ntoa(unpackedData[8])
    print('Source:\t\t\t', sourceAddress)
    distinationAddress = socket.inet_ntoa(unpackedData[9])
    print('Dist:\t\t\t', distinationAddress)
    playload = packet[20:]
    print('Pay load:\t\t', playload)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    
    return packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload  
    
#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    PacketCaptureBasedIDSAnalyze()