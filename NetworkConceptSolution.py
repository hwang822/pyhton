'''
Created on Jul 27, 2016
@author: Henry Wang
'''
import socket

#1. Ports and Protocols
#2. Address Resolution Protocol (ARP)
#3. Hypertext Transfer Protocol/Secure (HTTP/HTTPS)
#4. Domain Name System (DNS)
#5. Simple Mail Transfer Protocol (SMTP)
#6. Transmission Control Protocol/Open Systems Interconnect (TCP/OSI) Model 
#7. Sockets
#8. String-based Protocol
#9. Bitwise Protocol
#10. Internal Control Message Protocol (ICMP)
#11. Dynamic Host Configuration Protocol (DHCP)
#12. 802.1q
#13. Reading Request For Comments (RFC)


#1. Create socket with gieven Ports and Protocols
   #Create a given protocol socket to bind host address and given port.
   #127.0.0.1
def CreateIPSocket(port, protocol):
   s = None 
   
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol)
   s.bind(('',port))
   
   print ("CreateSocket(" + str(port) + ", " + str(protocol) + " protocol):" + str(s))

   return s

#2. Create socket with difference Address Resolution Protocol (ARP)
   #Create a socket with "Locus Address Resolution Protocol = 91" or "NARP, NBMA Address Resolution Protocol = 54" 
   #ARP (Address Resolution Protocol) is used to convert the IP address to its corresponding Ethernet (MAC) address. 
   #Retur socket infomation:<socket.socket fd=300, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=255, laddr=('0.0.0.0', 0)>"
def CreateARPSocket(arpProtocol):
   s = None
   
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, arpProtocol)
   socketInfo = str(s)
   print ("CreateARPSocket(" + str(arpProtocol) + "):" + str(s))
   
   return s


#3. Create HTTP Client as Hypertext Transfer Protocol/Secure (HTTP/HTTPS) for a given Host (example: www.python.org)
   #HTTP is a protocol that used for world wide web communication.
   #Create a connect to Host and send "GET" request to getresponse status "OK" 

import http.client
def CreateHTTPClient(host):
    conn = None

    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print (r1.status, r1.reason)
    data1 = r1.read()
    conn.request("GET", "/")
    r2 = conn.getresponse()
    print (r2.status, r2.reason)
    data2 = r2.read()
    conn.close()
	
    print("Connected to http: " + str(conn))
	
    return conn
	
#4. Resolve Domain Name System (DNS). Return IP address from a given host name (example: www.cnn.com => 151.101.56.73 ). 
def ResolveDNS(host):
   IPAddr = ''
   
   hostname, aliases, IPAddr  = socket.gethostbyname_ex(host)
   print (str(host) + " IP Address of the Domain Name is: "+repr(IPAddr))
   
   return IPAddr   

#5. Create socket with Simple Mail Transfer Protocol (SMTP)
   #The smtplib module defines an SMTP client session object that can be used to send mail. (example: send a test email to your email account).
   #Create smtpEmail and login your account to get return code => 235, b'2.7.0 Authentication succeeded'

import smtplib
def SendSTMPEamil():
   smtpEmail = None
   
   Authorized = ''   
   to = 'no_reply@email.com'
   hotmail_user = 'hotmail_username@hotmail.com'
   hotmail_pwd = 'hotmail_password'   
   smtpEmail = smtplib.SMTP("smtp.live.com",587)
   smtpEmail.ehlo()
   smtpEmail.starttls()
   smtpEmail.ehlo
   header = 'To:' + to + '\n' + 'From: ' + hotmail_user + '\n' + 'Subject:testing \n'
   print (header)
   msg = header + '\n this is test msg from my name \n\n'
   print (header)
   Authorized = smtpEmail.login(hotmail_user, hotmail_pwd)
   smtpEmail = smtpEmail.sendmail(hotmail_user, to, msg)
   print ('Authorized: ' + str(Authorized))   
   
   return smtpEmail, Authorized;
   
#6. Create socket with Transmission Control Protocol/Open Systems Interconnect (TCP/OSI) Model
   #in the server/client the socket module span layers 5 (session),6(presentation) and 7(application). More typically, the Internet Reference model compresses the OSI layers 5, 6, and 7 into a single layer called the Application Layer.

   #Create socket with
       #addressFamilies = socket.AF_UNIX, socket.AF_INET or socket.AF_INET6
       #socketTypes = socket.SOCK_STREAM, socket.SOCK_DGRAM or socket.SOCK_RAW
       #protocolType = socket.IPPROTO_IP or socket.IPPROTO_RAW       

       #SOCK_STREAM is using in TCP, SOCK_DGRAM is using for UDP.   
def CreateSocketofTCPandOSI(addressFamilies, socketTypes, protocolType):
   
   createdSocket = None
   
   createdSocket = socket.socket(addressFamilies, socketTypes, protocolType)
   print ("Created Socket:" + str(createdSocket))
   
   return createdSocket

#7. Create a Sockets
   #Cretee a default socket.
def CreateSocket():
   createdSocket = None
   
   createdSocket = socket.socket()
   print ("Created Socket:" + str(createdSocket))   

   return createdSocket
   
#8. Create socket String-based Protocol
   #Examples of text protocols: SMTP, HTTP, SIP.
   #Read text form a host web page.
def CreateTextProtocol(host):
    data1 = ''

    conn = http.client.HTTPSConnection(host)
    conn.request("GET", "/")
    r1 = conn.getresponse()
    print (r1.status, r1.reason)
    data1 = r1.read()
    #conn.request("GET", "/")
    #print("Data: " + str(data1[:100]))
    return data1 

#9. Create socket with difference Bitwise Protocol
   #Examples of binary protocols: RTP, TCP, IP.
   #Create a UDP socket to bind local host, sendto data to local host and socket will recvfrom data, addr from local host.
def CreateBinaryProtocol():
    s = None
        
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    host = socket.gethostbyname(socket.gethostname())
    s.bind((host, 0))
    s.sendto(b'Test', (host,0))	
    s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
#while 1:
    data, addr = s.recvfrom(1508)
    print("Packet from %r: %r" % (addr, data))
        
    return s

#10. Using Ping (ICMP) to check a server.
    #In Python, There is a way to ping a server through ICMP and return TRUE if the server responds, or FALSE if there is no response?
    #and then check the response...

import os
def PingServerThroughICMP(host):
    
    response = None
    
    hostname = host #example
    response = os.system("ping -c 1 " + hostname)
    
    if response == 0:
       print (hostname, 'is up!')
    else:
       print (hostname, 'is down!')
    
    return response

#11. Create get Dynamic Host Configuration Protocol (DHCP)
   #Dynamic Host Configuration Protocol (DHCP) is a client/server protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway.
   # the DHCP process workss as below:
   #1. The computer to connect to the Internet.
   #2. The network requests an IP address (this is actually referred to as a DHCP discover message).
   #3. On behalf of the computer's request, the DHCP server allocates (leases) to the computer an IP address. This is referred to as the DHCP offer message.
   #4. The computer (the the DHCP client) takes the first IP address offer that comes along. It then responds with a DHCP request message that verifies the IP address that's been offered and accepted.
   #5. DHCP then updates the appropriate network servers with the IP address and other configuration information for the computer.
   #6. The computer (or whatever network device using) accepts the IP address for the lease term.

def GetLocalDCHP(host):
    
    addr = None
    addr = socket.getaddrinfo(host, 80)[0][-1]
    print("IP Address: " + str(addr))
    return addr
	
#12. Create socket with 802.1q
   #socket.htons(0x8100)
   #IEEE 802.1Q is a protocol for carrying VLAN (Virtual Local Area Network) traffic on an Ethernet. 
   #Internet Protocol networks it is considered good practice to use a separate VLAN for each IP subnet. 
   #Ethernet frame Dest-MAC(6 bytes) + Src-MAC(6 bytes) +  801.1q-header(4 bytes)[tags Number] + EtherTypeSize(2 bytes) + plyBoard + CRC(4 pyes)
        #801.1q Header: Tag protocol identifier (TPID): a 16-bit field set to a value of 0x8100 (2 bytes)
        #               Tag control information (TCI) (2 bytes) 
                             #Priority code point (PCP): 3 bits
                             #Drop eligible indicator (DEI): 1 bit
                             #VLAN identifier (VID): 12-bits
                             
import struct
def CreateEthernetFrameWithVLANTag(src, dst, TPID, PCP, DEI, VID, eth_type,  payload, interface = b'eth0'):
    frame = None
    
    #802.1Q tag (TPID=0x8100, PCP=5, DEI=0, VID=3315)    
    tag = struct.pack('BB', (PCP<<5 & 0xE0) + (DEI<<4 & 0x10) + (VID>>8 & 0xF), (VID & 0xFF))
    
    print("Tag: " + str(tag))
        
    frame = src + dst + TPID + tag + eth_type + payload 
    
    print(frame)
   
    return frame
    
#13 Create socket with difference Reading Request For Comments (RFC)

import requests  #pip install requests to have request.
def ReadingRequestForComments(requestComments):
    
    requestGet = None
            
    requestGet = requests.get(requestComments)
    print("\nStats: " + str(requestGet.status_code))
    print("\nHeader: " + str(requestGet.headers))
    print("\nContent: " + requestGet.content[:20].decode())	
	
    return requestGet
	

#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
    CreateIPSocket(0, socket.IPPROTO_RAW)   #1
    CreateARPSocket(54)						#2
    CreateHTTPClient('www.python.org')      #3
    ResolveDNS('www.cnn.com')	    		#4
    SendSTMPEamil()                         #5
    CreateSocketofTCPandOSI(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)               #6
    CreateSocket()                          #7
    CreateTextProtocol('www.python.org')    #8
    CreateBinaryProtocol()                  #9
    PingServerThroughICMP('www.google.com')	#10
    GetLocalDCHP('micropython.org')         #11
    CreateEthernetFrameWithVLANTag(b'\xFE\xED\xFA\xCE\xBE\xEF', b'\xFE\xED\xFA\xCE\xBE\xEF', b'\x81\x00', 5, 0, 3315, b'\x08\x00', b'hello', 'eth0')   #12	
    ReadingRequestForComments('https://www.google.com/') #13	

	
