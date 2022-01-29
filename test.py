print('\nRunning test.py...\n')

mac_addresses = ('49:42:08:00:5C:61', '49:42:08:00:50:D7', '49:42:08:00:5E:A4')
MAC_ADDRESS_INDEX = 0

from inkbird import InkbirdIBSTH

mac_address = mac_addresses[MAC_ADDRESS_INDEX]
sensor_type = 'Inkbird_IBSTH2'

inkbird = InkbirdIBSTH(mac_address, sensor_type)
reading = inkbird.read_sensor()
print('Reading successful.\n')
[print(f'{k}: {v}') for k,v in reading.items()]
