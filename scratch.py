from inkbird.inkbird import InkbirdIBSTH

mac_address = '49:42:08:00:5C:61'
#mac_address = '49:42:08:00:50:D7'
sensor_type = 'Inkbird_IBSTH2'
inkbird = InkbirdIBSTH(mac_address, sensor_type)
v = inkbird.get_ibsth_data()
print(v)

