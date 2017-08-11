'''
Created on Aug 9, 2016
@author: Henry Wang
python -m compileall PacketCaptureBasedIDSTest.py

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
import unittest

from PacketCaptureBasedIDS import PacketCaptureBasedIDSAnalyze

#Test PacketCaptureBasedIDS funxtion returned packet information.
class TestPacketCaptureBasedIDSAnalyze(unittest.TestCase):
    def test_PacketCaptureBasedIDSAnalyze(self):
        packet, receiveraddress, version, IHL, totallength, ID, protocol, sourceAddress, distinationAddress, playload = PacketCaptureBasedIDSAnalyze()
    
        unpackedData = struct.unpack('!BBHHHBBH4s4s', packet[:20])	    
      # print('UnpackedData: ', unpackedData)
	  
	  
	  #!{ network, B: integer 1byte, H unsigned short 2byte, s char[n]  1+1+2+2+2+1+1+2+4+4 = 20
	  # B => Version, IHL  B=> Differentiated Services, H=> Total Length
      # H => Identification   H => Flags, Fragment Offset	  
	  # B = TTL B=> Protocol, H =>Header checsum. 
 	  # 4s => Source IP address   4s => Destination IP Addresss
	  	 
        version_IHL = unpackedData[0]
        version1 = unpackedData[0] >> 4
        TOS1 = unpackedData[1]
        totallength1 = unpackedData[2]
        ID1 = unpackedData[3]
        protocol1 = unpackedData[6]
        sourceAddress1 = socket.inet_ntoa(unpackedData[8])
        distinationAddress1 = socket.inet_ntoa(unpackedData[9])
        playload1 = packet[20:]

        self.assertIsNotNone(packet)
        self.assertEqual(version, version1)
        self.assertEqual(totallength, totallength1)
        self.assertEqual(ID, ID1)
        self.assertEqual(protocol, protocol1)
        self.assertEqual(sourceAddress, sourceAddress1)
        self.assertEqual(distinationAddress, distinationAddress1)
        self.assertEqual(playload, playload1)

        self.assertEqual(receiveraddress[0], sourceAddress)
        self.assertEqual(IHL, 20)
        self.assertEqual(totallength, len(packet))
    
if __name__ == '__main__':
    unittest.main(exit=False) 
