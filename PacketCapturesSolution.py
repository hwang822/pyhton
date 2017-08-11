'''
Created on Jul 13, 2016
@author: Henry Wang

'''

import socket
import sys

#Create a ROW PACKET socket ( host = 'localhost', port = 0, Socket Type = socket.SOCK_RAW) which will send a packet including ip_header(20 bytes) and sendMessage. The socket will bind to local HOST server = (HOST, 0). Using creted socket.sendto(sendMessage, server) to Local HOST server. return created socket.
def PacketCapacureConnection(sendMessage):
#code will be hidden
   try:
      ROWSocket = None
      host = socket.gethostname()
      port = 0
      server = (host, port) # need same port at server
      print ("Connect to server:" + str(host) + ", " + str(port))
      ROWSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)	
      ROWSocket.bind(server)	
      ROWSocket.sendto(sendMessage.encode(), server)
      print("Conection Host Scussfully.")
      return ROWSocket
   except:
      print('Conection Host Failure.')

#Recall PacketCapacureConnection(sendMessage) to get socket and send message to Local HOST server, using socket to read data from Local HOST server. 
#return received data size.	  
def PacketCapacureDataSize(sendMessage):
   lenMessage = 0

#code will be hidden   
   ROWSocket = PacketCapacureConnection(sendMessage)
   data, addr = ROWSocket.recvfrom(65565)   
   lenMessage = len(data)
   print('Packet Size: {}'.format(lenMessage))
   
   return lenMessage
	  
#Recall PacketCapacureConnection(sendMessage) to get socket and send message to Local HOST server, using socket to read data from Local HOST server. 
#return received data from string behind 20 bytes IP_header of data.	  	  
def PacketCapacureData(sendMessage):
   recvMessage = ''   

#code will be hidden   
   ROWSocket = PacketCapacureConnection(sendMessage)
   data, addr = ROWSocket.recvfrom(65565)
   recvMessage = data[20:]   
   print('Packet Data: {}'.format(recvMessage))   
   
   return recvMessage
	  
#Create command line able to call above functions with given snedMessage.	  
if __name__ == '__main__':
#code will be hidden

    sendMessage = sys.argv[1]	
    PacketCapacureConnection(sendMessage)
    PacketCapacureData(sendMessage)
    PacketCapacureDataSize(sendMessage)
    PacketCapacureSourceAddr(sendMessage)