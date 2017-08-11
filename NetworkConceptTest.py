'''
Created on Aug 1, 2016
@author: Henry Wang

'''
import socket
import unittest
import http.client
import requests  #pip install requests to have request.

from NetworkConcept import CreateSocket, CreateIPSocket, CreateARPSocket, CreateHTTPClient, ResolveDNS, PingServerThroughICMP, GetLocalDCHP
from NetworkConcept import SendSTMPEamil,ReadingRequestForComments, CreateTextProtocol, CreateBinaryProtocol, CreateSocketofTCPandOSI, CreateEthernetFrameWithVLANTag

#1. Create socket with gieven Ports and Protocols
   #Create a given protocol socket to bind host address and given port.
   
#Create a given protocol socket to bind host address and given port.
class TestNetworkConcept(unittest.TestCase):
   def test_TestCreateIPSocket(self):
      s = CreateIPSocket(0, socket.IPPROTO_RAW)
      self.assertIsNotNone(s)
      self.assertEqual(s.proto, socket.IPPROTO_RAW)

#2. Create socket with difference Address Resolution Protocol (ARP)
   #Create a socket with "Locus Address Resolution Protocol = 91" or "NARP, NBMA Address Resolution Protocol = 54" 
   #ARP (Address Resolution Protocol) is used to convert the IP address to its corresponding Ethernet (MAC) address. 
   #Retur socket infomation:<socket.socket fd=300, family=AddressFamily.AF_INET, type=SocketKind.SOCK_RAW, proto=255, laddr=('0.0.0.0', 0)>"
   def test_TestCreateARPSocket(self):
      s = CreateARPSocket(91)
      self.assertIsNotNone(s)
      self.assertEqual(s.proto, 91)
      s = CreateARPSocket(54)
      self.assertIsNotNone(s)
      self.assertEqual(s.proto, 54)

#3. Create HTTP Client as Hypertext Transfer Protocol/Secure (HTTP/HTTPS) for a given Host (example: www.python.org)
   #HTTP is a protocol that used for world wide web communication.
   #Create a connect to Host and send "GET" request to getresponse status "OK" 
   def test_TestCreateHTTPClient(self):
      conn = CreateHTTPClient('www.python.org')
      self.assertIsNotNone(CreateHTTPClient('www.python.org'))	  
      
      conn.request("GET", "/")
      r1 = conn.getresponse()
      self.assertEqual(r1.status, 200)
      self.assertEqual(r1.reason, 'OK')
            	  
#4. Resolve Domain Name System (DNS). Return IP address from a given host name (example: www.cnn.com => 151.101.56.73). 
   def test_TestResolveDNS(self):
      hostname, aliases, IPAddr = socket.gethostbyname_ex('www.cnn.com')
      self.assertEqual(ResolveDNS('www.cnn.com'), IPAddr)

#5. Create socket with Simple Mail Transfer Protocol (SMTP)
   #The smtplib module defines an SMTP client session object that can be used to send mail. (example: send a test email to your email account).
   #Create smtpEmail and login your account to get return code => 235, b'2.7.0 Authentication succeeded'   
   def test_TestSendSTMPEamil(self):
      smtpEmail, Authertied = SendSTMPEamil()      
      self.assertIsNotNone(smtpEmail)
      self.assertEqual(Authertied, (235, b'2.7.0 Authentication succeeded'))
      
#6. Create socket with Transmission Control Protocol/Open Systems Interconnect (TCP/OSI) Model
   #in the server/client python utilize the socket module span layers 5 (session),6(presentation) and 7(application). python code utilizes sockets as presenting data, managing sessions and creating sockets using transport protocols such as tcp or udp. 
   #the OSI model is not commonly used in practice. More typically, the Internet Reference model compresses the OSI layers 5, 6, and 7 into a single layer called the Application Layer.
   #SOCK_STREAM is using in TCP, SOCK_DGRAM is using for UDP.

   def test_TestCreateSocketofTCPandOSI(self):
      s = CreateSocketofTCPandOSI(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IP)            
      self.assertIsNotNone(s)
      self.assertEqual(s.family, socket.AF_INET)
      self.assertEqual(s.type, socket.SOCK_DGRAM)
      self.assertEqual(s.proto, socket.IPPROTO_IP)
   
#7. Create a Sockets
   #create a default 
   #Retur socket infomation: "<socket.socket fd=328, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>".
   
   def test_TestCreateSocket(self):
      s = CreateSocket()            
      self.assertIsNotNone(s)

#8. Create socket String-based Protocol
   #Examples of text protocols: SMTP, HTTP, SIP.
   #Read text form a host web page.
      
   def test_TestCreateTextProtocol(self):
      data1 = CreateTextProtocol('www.python.org')      
      conn = http.client.HTTPSConnection('www.python.org')          
      conn.request("GET", "/")
      r2 = conn.getresponse()
      data2 = r2.read()
      self.assertEqual(data1, data2)

      
#9. Create socket with difference Bitwise Protocol
   #Examples of binary protocols: RTP, TCP, IP.
   #Create a UDP socket to bind local host, sendto given text to local host and socket will recvfrom header + text from local host.
   def test_TestCreateBinaryProtocol(self):
      s = CreateBinaryProtocol()      
      self.assertIsNotNone(s)  
      
      
#10. Using Ping (ICMP) to check a server.
    #In Python, There is a way to ping a server through ICMP and return TRUE if the server responds, or FALSE if there is no response?
    #and then check the response...
   def test_TestPingServerThroughICMP(self):      
      self.assertEqual(PingServerThroughICMP('www.google.com'), 0)
	  
#11. Create get Dynamic Host Configuration Protocol (DHCP)
   #Dynamic Host Configuration Protocol (DHCP) is a client/server protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway.
   # the DHCP process workss as below:
   #1. The computer to connect to the Internet.
   #2. The network requests an IP address (this is actually referred to as a DHCP discover message).
   #3. On behalf of the computer's request, the DHCP server allocates (leases) to the computer an IP address. This is referred to as the DHCP offer message.
   #4. The computer (the the DHCP client) takes the first IP address offer that comes along. It then responds with a DHCP request message that verifies the IP address that's been offered and accepted.
   #5. DHCP then updates the appropriate network servers with the IP address and other configuration information for the computer.
   #6. The computer (or whatever network device using) accepts the IP address for the lease term.

   def test_TestGetLocalDCHP(self):      
      self.assertEqual(GetLocalDCHP('www.google.com'), socket.getaddrinfo('www.google.com', 80)[0][-1])
	      
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

   def test_TestCreateEthernetFrameWithVLANTag(self):      
      self.assertEqual(CreateEthernetFrameWithVLANTag(b'\xFE\xED\xFA\xCE\xBE\xEF', b'\xFE\xED\xFA\xCE\xBE\xEF', b'\x81\x00', 5, 0, 3315, b'\x08\x00', b'hello', 'eth0'), b'\xfe\xed\xfa\xce\xbe\xef\xfe\xed\xfa\xce\xbe\xef\x81\x00\xac\xf3\x08\x00hello')
                             
#13 Create socket with difference Reading Request For Comments (RFC)

   def test_TestReadingRequestForComments(self):      
      self.assertEqual(str(ReadingRequestForComments('https://www.google.com/')), str(requests.get('https://www.google.com/')))
          
          
'''	  
   def test_TestReadingRequestForComments(self):
      self.assertIsNotNone(ReadingRequestForComments('https://www.google.com/'))
	  
'''

if __name__ == '__main__':
   unittest.main(exit=False) 