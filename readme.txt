1. Packet Captures function and test.

   PacketCapacureConnection(sendMessage)
      Create a ROW PACKET socket (host = 'localhost', port = 0, socket type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
      Test created ROW PACKET socket.
   PacketCapacureData(sendMessage)
      Recall PacketCapacureConnection(sendMessage) to get socket and send message to Local HOST server, using socket to read data from Local HOST server. return received data from string behind 20 bytes IP_header of data
      Test captured message will same as given message.
   PacketCapacureDataSize(sendMessage) 
      Recall PacketCapacureConnection(sendMessage) to get socket and send message to Local HOST server, using socket to read data from Local HOST server. return received data size.
	  Test captured message size will equal to IP_Header size (20 bytes) + given message size.

2. Packet Analysis function and test.
    PacketsAnalysis(givenMessage)
       Create a ROW PACKET socket (host = 'localhost', port = 0, socket type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
       Receive a packet from the created socket of local host with IPheader + Message + Address.
       Unpacket IPHeader as below table for analysis.
   	   Test captured message and header will same as given message and expected header information.   
	  
3. Packet Captures Filter function and test.
    PacketsCaptureFilter(givenMessage)
       Create a ROW PACKET socket (host = 'localhost', port = 0, socket type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
       Receive a packet from the created socket of local host with IPheader + Message + Address.
       Unpacket IPHeader as below table for filter.
   	   Test captured message and header to cmpare the filter values.   	  

4. Network Concepts funcition and test.
   #1. Ports and Protocols - Create a given protocol socket to bind host address and given port.
   #2. Address Resolution Protocol (ARP) - Create a socket with "Locus Address Resolution Protocol = 91" or "NARP, NBMA Address Resolution Protocol = 54"
   #3. Hypertext Transfer Protocol/Secure (HTTP/HTTPS) - Create a connect to Host and send "GET" request to getresponse status "OK".
   #4. Domain Name System (DNS) - Resolve Domain Name System (DNS). Return IP address from a given host name.
   #5. Simple Mail Transfer Protocol (SMTP) - Create smtpEmail and login your account to get return code => 235, b'2.7.0 Authentication succeeded'
   #6. Transmission Control Protocol/Open Systems Interconnect (TCP/OSI) Model - Create socket with Transmission Control Protocol/Open Systems Interconnect (TCP/OSI) Model.
   #7. Sockets - Cretee a default socket.
   #8. String-based Protocol - Create socket String-based Protocol (HTTP), Read text form a host web page.
   #9. Bitwise Protocol - Create socket with difference Bitwise Protocol, Set UDP socket to bind local host, sendto data to local host and socket will recvfrom data, addr from local host.  
   #10. Internal Control Message Protocol (ICMP) - Using Ping (ICMP) to check a host server
   #11. Dynamic Host Configuration Protocol (DHCP) - Create get Dynamic Host Configuration Protocol (DHCP) to get local host IP address.
   #12. 802.1q - Create a Ethernet frame with 802.1q (VLAN Tags).  
   #13. Reading Request For Comments (RFC) - Create socket with difference Reading Request For Comments (RFC).
	  
5. Packet Capture (PCAP) based Intrusion Detection System (IDS) Analysis
   Create RAW socket and bind to (localhost, 0). recvfrom packet (header + playload), parse IPheader then reutrn packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload for test analyze   

6. Secure vs Non-secure Traffic (encrypted vs non-encrypted)
   Create TCP server to verify client user name and password
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
