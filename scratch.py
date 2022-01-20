mac_addresses = ('49:42:08:00:5C:61', '49:42:08:00:50:D7')
MAC_ADDRESS_INDEX = 0

from inkbird import InkbirdIBSTH

mac_address = mac_addresses[MAC_ADDRESS_INDEX]
sensor_type = 'Inkbird_IBSTH2'

inkbird = InkbirdIBSTH(mac_address, sensor_type)
reading = inkbird.get_ibsth_data()
print(reading)
