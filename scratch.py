import os
import json
import yaml

from inkbird import InkbirdIBSTH

print(f'pwd is: {os.getcwd()}\n')
class THMonitor():
    def __init__(self, config_yaml='sensors.yaml'):
        with open(config_yaml) as file:
            yaml_content = yaml.safe_load(file)
        for d in yaml_content['sensors']:
            d['device'] = InkbirdIBSTH(d['mac_address'], d['sensor_type'])
        self.sensors = yaml_content['sensors']
        

    def get_sensor_data(self):
        for d in self.sensors:
            d['last_reading'] = d['device'].get_ibsth_data()
            
thm = THMonitor()
thm.get_sensor_data()

print(json.dumps(thm.sensors, indent=2, default=str))
    
from bluepy import btle
import struct


        
mac_addresses = ('49:42:08:00:5C:61', '49:42:08:00:50:D7')
MAC_ADDRESS_INDEX = 0

#from inkbird import InkbirdIBSTH

mac_address = mac_addresses[MAC_ADDRESS_INDEX]
sensor_type = 'Inkbird_IBSTH2'

inkbird = InkbirdIBSTH(mac_address, sensor_type)
p = inkbird.peripheral
c = p.getCharacteristics()
import sys

for i in c:
    if i.supportsRead():
        print(
            sys.getsizeof(i.read()),
            i.read(),
            i.getDescriptors(),
            i.getHandle(),
            i.propertiesToString(),
            i.supportsRead(),
        )
    else:
        print('non-readable characteristic')
        
        
        
mac_addresses = ('49:42:08:00:5C:61', '49:42:08:00:50:D7')
MAC_ADDRESS_INDEX = 1
mac_address = mac_addresses[MAC_ADDRESS_INDEX]     
from bluepy import btle
peripheral = btle.Peripheral(mac_address)
p = peripheral
