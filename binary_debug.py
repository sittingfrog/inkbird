mac_addresses = ('49:42:08:00:5C:61', '49:42:08:00:50:D7', '49:42:08:00:5E:A4')
MAC_ADDRESS_INDEX = 0

REQ_BATTERY_MESSAGE = bytes([0x08, 0x24, 0x00, 0x00, 0x00, 0x00])

import sys
import struct
from inkbird import InkbirdIBSTH

mac_address = mac_addresses[MAC_ADDRESS_INDEX]
sensor_type = 'Inkbird_IBSTH2'

inkbird = InkbirdIBSTH(mac_address, sensor_type)

def print_characteristic_info(characteristic):
    c = characteristic
    if c.supportsRead():
        print(
            f'size: {sys.getsizeof(c.read())}',
            f'bytes: {c.read()}',
            f'descriptors: {[d.read() for d in c.getDescriptors()]}',
            f'handle: {c.getHandle()}',
            f'properties: {c.propertiesToString()}',
            f'supports read: {c.supportsRead()}',
            sep='\n'
        )
    else:
        print('non-readable characteristic')

def list_characteristics(characteristics):
    for characteristic in characteristics:
        print_characteristic_info(characteristic)
           
c = inkbird.sensor_characteristics
#list_characteristics(c)
i = 2
print_characteristic_info(c[i])

format_binary = '=HHHH'
valueBinary = c[i].read()
unpacked = struct.unpack(format_binary, valueBinary)

print(unpacked)
