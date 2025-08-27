##################
'''
This code is written based on https://github.com/MuffinSpawn/Leica/
'''

##################

import struct

class PacketHeaderT:
    def __init__(self):
        self.packet = b''
        self.__packet_size = 8
        self.__sizes = [8] #複数種類のサイズのパケットが来たときに対応できるようにリストにしている
        self.__formats = [('<i I ')]
        self.lPacketSize = int(0)
        self.type = int(0) #ES_DatType

    def to_binary(self):
        self.packet = b''
        packet_elements = ()
        packet_elements +=(self.lPacketSize,)
        packet_elements +=(self.type,)
        self.packet += struct.Struct(self.__format[0].pack(*packet_elements))
        retun self.packet

    def from_binary(self, packet):
        self.packet = packet
        packet_elements = struct.Struct(self.__formats[0]).unpack(packet[:self.__size[0]])
        self.lPacketSize = packet_elements[0]
        self.type = packet_elements[1]
        return packet[self.__sizes[0]:]
        


class BasicCommandCT:
    def __init__(self):
        self.packet = b''
        self.__packet_size =12
        self.__sizes =[4]
        self.__formats
        self.__formats = [('<I ')]
        self.packetHeader = PacketHeaderT()
        self.command = int(0)




